
import os
import qrcode

from functools import wraps

from flask import (
    Flask,
    render_template,
    request,
    redirect,
    url_for,
    flash,
    abort
)

from flask_login import (
    LoginManager,
    login_user,
    logout_user,
    login_required,
    current_user
)

from werkzeug.security import (
    generate_password_hash,
    check_password_hash
)

from sqlalchemy.exc import IntegrityError

from models import db, User, BusRoute, Booking
from config import Config


# APPLICATION CONFIGURATION
app = Flask(__name__)
app.config.from_object(Config)

db.init_app(app)

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = "login"


# STAFF ACCESS CONTROL
def staff_required(view_function):

    @wraps(view_function)
    @login_required
    def decorated_function(*args, **kwargs):

        if not current_user.is_staff:
            abort(403)

        return view_function(*args, **kwargs)

    return decorated_function


# USER SESSION MANAGEMENT
@login_manager.user_loader
def load_user(user_id):

    return db.session.get(User, int(user_id))


# HOME PAGE
@app.route("/")
def home():

    return render_template("index.html")


# USER REGISTRATION
@app.route("/register", methods=["GET", "POST"])
def register():

    if current_user.is_authenticated:
        return redirect(url_for("routes"))

    if request.method == "POST":

        username = request.form.get(
            "username", ""
        ).strip()

        email = request.form.get(
            "email", ""
        ).strip().lower()

        password = request.form.get(
            "password", ""
        )

        if not username or not email or not password:

            flash(
                "All fields are required.",
                "error"
            )

        elif len(password) < 8:

            flash(
                "Password must contain at least 8 characters.",
                "error"
            )

        elif User.query.filter_by(email=email).first():

            flash(
                "Email already registered.",
                "error"
            )

        else:

            user = User(
                username=username,
                email=email,
                password=generate_password_hash(password),
                is_staff=False
            )

            db.session.add(user)

            try:

                db.session.commit()

                flash(
                    "Registration successful! Please login.",
                    "success"
                )

                return redirect(url_for("login"))

            except IntegrityError:

                db.session.rollback()

                flash(
                    "This email is already registered.",
                    "error"
                )

            except Exception:

                db.session.rollback()

                app.logger.exception(
                    "Registration failed."
                )

                flash(
                    "Registration failed. Please try again.",
                    "error"
                )

    return render_template("register.html")


# USER LOGIN
@app.route("/login", methods=["GET", "POST"])
def login():

    if current_user.is_authenticated:
        return redirect(url_for("routes"))

    if request.method == "POST":

        email = request.form.get(
            "email", ""
        ).strip().lower()

        password = request.form.get(
            "password", ""
        )

        user = User.query.filter_by(
            email=email
        ).first()

        if user and check_password_hash(
            user.password,
            password
        ):

            login_user(user)

            flash(
                "Login successful!",
                "success"
            )

            return redirect(url_for("routes"))

        flash(
            "Invalid email or password.",
            "error"
        )

    return render_template("login.html")


# USER LOGOUT
@app.route("/logout", methods=["GET", "POST"])
@login_required
def logout():

    logout_user()

    flash(
        "You have logged out successfully.",
        "success"
    )

    return redirect(url_for("home"))


# DISPLAY AVAILABLE BUS ROUTES
@app.route("/routes")
@login_required
def routes():

    all_routes = BusRoute.query.order_by(
        BusRoute.id
    ).all()

    return render_template(
        "routes.html",
        routes=all_routes
    )


# GENERATE QR CODE
def generate_ticket_qr(ticket_id):

    qr_folder = os.path.join(
        app.static_folder,
        "qrcodes"
    )

    os.makedirs(
        qr_folder,
        exist_ok=True
    )

    qr = qrcode.QRCode(
        version=1,
        box_size=10,
        border=4
    )

    verification_url = url_for(
        "verify_ticket",
        ticket_id=ticket_id,
        _external=True
    )

    qr.add_data(verification_url)

    qr.make(fit=True)

    image = qr.make_image(
        fill_color="black",
        back_color="white"
    )

    image.save(
        os.path.join(
            qr_folder,
            f"{ticket_id}.png"
        )
    )


# BOOK A BUS SEAT
@app.route("/book/<int:route_id>", methods=["POST"])
@login_required
def book(route_id):

    route = db.session.get(
        BusRoute,
        route_id
    )

    if not route:
        abort(404)

    try:

        seat_number = int(
            request.form.get("seat_number", "")
        )

    except (ValueError, TypeError):

        flash(
            "Please enter a valid seat number.",
            "error"
        )

        return redirect(url_for("routes"))

    if seat_number < 1 or seat_number > route.total_seats:

        flash(
            "Invalid seat number.",
            "error"
        )

        return redirect(url_for("routes"))

    existing = Booking.query.filter_by(
        route_id=route.id,
        seat_number=seat_number
    ).first()

    if existing:

        flash(
            "This seat is already booked.",
            "error"
        )

        return redirect(url_for("routes"))

    booking = Booking(
        user_id=current_user.id,
        route_id=route.id,
        seat_number=seat_number
    )

    try:

        db.session.add(booking)
        db.session.commit()

    except IntegrityError:

        db.session.rollback()

        flash(
            "This seat was just booked by another passenger. Please select another seat.",
            "error"
        )

        return redirect(url_for("routes"))

    except Exception:

        db.session.rollback()

        app.logger.exception(
            "Booking failed."
        )

        flash(
            "Booking failed. Please try again.",
            "error"
        )

        return redirect(url_for("routes"))

    # GENERATE QR AFTER SUCCESSFUL BOOKING
    try:

        generate_ticket_qr(
            booking.ticket_id
        )

    except Exception:

        app.logger.exception(
            "QR generation failed."
        )

        flash(
            "Booking saved, but QR generation failed. Please contact support.",
            "error"
        )

        return redirect(
            url_for("my_bookings")
        )

    flash(
        "Your ticket has been booked successfully!",
        "success"
    )

    return redirect(
        url_for("my_bookings")
    )


# USER DIGITAL TICKETS
@app.route("/my-bookings")
@login_required
def my_bookings():

    bookings = Booking.query.filter_by(
        user_id=current_user.id
    ).order_by(
        Booking.booking_date.desc()
    ).all()

    return render_template(
        "bookings.html",
        bookings=bookings
    )


# TICKET VERIFICATION
@app.route("/verify/<ticket_id>")
@login_required
def verify_ticket(ticket_id):

    if current_user.is_staff:

        booking = Booking.query.filter_by(
            ticket_id=ticket_id
        ).first_or_404()

    else:

        booking = Booking.query.filter_by(
            ticket_id=ticket_id,
            user_id=current_user.id
        ).first_or_404()

    return render_template(
        "verify.html",
        booking=booking
    )


# STAFF-ONLY QR CAMERA SCANNER
@app.route("/scan")
@staff_required
def scan_qr():

    return render_template(
        "scanner.html"
    )


# DATABASE INITIALIZATION
with app.app_context():

    db.create_all()

    if BusRoute.query.count() == 0:

        demo_routes = [

            BusRoute(
                source="Islamabad",
                destination="Lahore",
                departure_time="08:00 AM",
                price=2500,
                total_seats=40
            ),

            BusRoute(
                source="Rawalpindi",
                destination="Faisalabad",
                departure_time="10:00 AM",
                price=1800,
                total_seats=40
            ),

            BusRoute(
                source="Lahore",
                destination="Multan",
                departure_time="02:00 PM",
                price=1500,
                total_seats=40
            )

        ]

        db.session.add_all(demo_routes)
        db.session.commit()


# RUN APPLICATION
if __name__ == "__main__":

    app.run(
        host="127.0.0.1",
        port=5000,
        debug=True
    )
