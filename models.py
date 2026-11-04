
from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin
from sqlalchemy import UniqueConstraint
from datetime import datetime
import uuid

db = SQLAlchemy()


# USER MODEL
class User(UserMixin, db.Model):

    id = db.Column(
        db.Integer,
        primary_key=True
    )

    username = db.Column(
        db.String(100),
        nullable=False
    )

    email = db.Column(
        db.String(120),
        unique=True,
        nullable=False
    )

    password = db.Column(
        db.String(255),
        nullable=False
    )

    # Passenger = False, Staff = True
    is_staff = db.Column(
        db.Boolean,
        default=False,
        nullable=False
    )


# BUS ROUTE MODEL
class BusRoute(db.Model):

    id = db.Column(
        db.Integer,
        primary_key=True
    )

    source = db.Column(
        db.String(100),
        nullable=False
    )

    destination = db.Column(
        db.String(100),
        nullable=False
    )

    departure_time = db.Column(
        db.String(50),
        nullable=False
    )

    price = db.Column(
        db.Float,
        nullable=False
    )

    total_seats = db.Column(
        db.Integer,
        default=40
    )


# BOOKING MODEL
class Booking(db.Model):

    __table_args__ = (
        UniqueConstraint(
            "route_id",
            "seat_number",
            name="uq_booking_route_seat"
        ),
    )

    id = db.Column(
        db.Integer,
        primary_key=True
    )

    ticket_id = db.Column(
        db.String(36),
        unique=True,
        default=lambda: str(uuid.uuid4())
    )

    user_id = db.Column(
        db.Integer,
        db.ForeignKey("user.id"),
        nullable=False
    )

    route_id = db.Column(
        db.Integer,
        db.ForeignKey("bus_route.id"),
        nullable=False
    )

    seat_number = db.Column(
        db.Integer,
        nullable=False
    )

    booking_date = db.Column(
        db.DateTime,
        default=datetime.utcnow
    )

    user = db.relationship(
        "User",
        backref="bookings"
    )

    route = db.relationship(
        "BusRoute",
        backref="bookings"
    )
