# 🚌 CloudBus — Smart Bus Pass Management System

<p align="center">
  <strong>A Secure, QR-Based Digital Bus Pass Management Platform</strong>
  <br/>
  Built with Python, Flask, SQLite, and modern web technologies.
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.x-blue?logo=python&logoColor=white" alt="Python"/>
  <img src="https://img.shields.io/badge/Flask-Web%20Framework-black?logo=flask" alt="Flask"/>
  <img src="https://img.shields.io/badge/Database-SQLite-blue?logo=sqlite&logoColor=white" alt="SQLite"/>
  <img src="https://img.shields.io/badge/Authentication-Flask--Login-green" alt="Authentication"/>
  <img src="https://img.shields.io/badge/QR%20Code-Ticket%20Verification-purple" alt="QR Code"/>
  <img src="https://img.shields.io/badge/Status-Development-orange" alt="Development"/>
</p>

---

## 🚀 Overview

**CloudBus** is a web-based bus pass management system designed to simplify digital ticket booking and passenger verification.

The platform provides a convenient way for passengers to register, explore available routes, reserve seats, and receive QR-based digital tickets. Authorized staff members can scan and verify tickets through a dedicated verification interface.

The project focuses on secure authentication, role-based authorization, booking integrity, and practical digital transportation workflows.

## ✨ Key Features

### 👤 Passenger Management
- User registration and secure login.
- Password hashing for account security.
- Browse available bus routes.
- Book seats for selected routes.
- View personal booking records.
- Access digital tickets with QR codes.

### 🛡️ Staff Management
- Dedicated staff account authorization.
- Restricted access to the QR scanner.
- Scan passenger QR tickets.
- Verify ticket information.
- Access ticket verification functionality.

### 🔐 Security Features
- Password hashing using Werkzeug.
- Session management with Flask-Login.
- Role-based access control.
- Staff-only scanner authorization.
- Passenger ticket ownership protection.
- Database-level duplicate seat booking prevention.
- Environment-based secret key configuration.
- Sensitive files excluded through `.gitignore`.

### 📱 QR-Based Ticket Verification
- Automatic QR code generation for bookings.
- Browser-based QR scanning.
- Dedicated ticket verification endpoint.
- Ticket ownership and authorization checks.

## 🧰 Technology Stack

| Technology | Purpose |
|---|---|
| Python | Backend programming |
| Flask | Web application framework |
| Flask-SQLAlchemy | Database integration |
| SQLite | Database storage |
| Flask-Login | User authentication |
| Werkzeug | Password hashing |
| HTML5 | Frontend structure |
| CSS3 | Responsive interface styling |
| JavaScript | Frontend interactions |
| QR Code | Digital ticket generation |
| html5-qrcode | Browser-based QR scanning |
| Git & GitHub | Version control |

## 🏗️ System Architecture

```text
                 CLOUD BUS PLATFORM
                         |
             +-----------+-----------+
             |                       |
        Passenger Portal         Staff Portal
             |                       |
      Registration/Login       Staff Authentication
             |                       |
       Browse Routes           QR Scanner
             |                       |
        Seat Booking           Ticket Verification
             |                       |
       QR Ticket Generation ---------+
             |
       SQLite Database
             |
       Booking Records
```

## 📂 Project Structure

```text
Cloud-Based-Bus-Pass-System/
│
├── app.py
├── config.py
├── models.py
├── requirements.txt
├── .env.example
├── .gitignore
│
├── templates/
│   ├── index.html
│   ├── login.html
│   ├── register.html
│   ├── routes.html
│   ├── bookings.html
│   ├── scanner.html
│   └── verify.html
│
├── static/
│   ├── css/
│   ├── js/
│   ├── images/
│   └── qrcodes/
│
└── instance/
    └── buspass.db
```

*Note: The database and generated QR files are excluded from the public repository.*

## ⚙️ Installation & Setup

Follow these steps to run CloudBus locally.

### 1. Clone the repository

```bash
git clone https://github.com/rashidabdullah5737-ai/Cloud-Based-Bus-Pass-System.git
cd Cloud-Based-Bus-Pass-System
```

### 2. Create a virtual environment

```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure environment variables

```bash
cp .env.example .env
```

Generate a secure secret key:

```bash
python -c "import secrets; print(secrets.token_urlsafe(48))"
```

Add the generated value to your `.env` file:

```env
SECRET_KEY=your_generated_secret_key
```

Never publish your actual `.env` file or secret key.

### 5. Start the application

```bash
python app.py
```

Open the local application in your browser at:

```text
http://127.0.0.1:5000
```

*If your application uses a different startup command or port, use the configuration defined in `app.py`.*

## 🔍 Security & Testing

The following security and functional checks were performed during development:

| Test | Expected Result |
|---|---|
| User registration | Successful account creation |
| User login | Authenticated session |
| Staff login | Authorized staff access |
| Passenger QR ticket | QR ticket generated |
| Ticket verification | Ticket details verified |
| Passenger ticket ownership | Unauthorized access blocked |
| Passenger access to staff scanner | HTTP 403 Forbidden |
| Duplicate seat booking | Database uniqueness protection |

### Security Design Highlights

- Passengers cannot access staff-only scanning functionality.
- Users are restricted from accessing other passengers' protected ticket information.
- Database uniqueness protection helps prevent duplicate bookings for the same route and seat.
- Application secrets and local database files are kept outside the public Git repository.

## 🔮 Future Improvements

- Cloud deployment and managed database integration.
- Online payment gateway.
- Live bus tracking and GPS integration.
- Email and SMS booking notifications.
- Administrative analytics dashboard.
- Automated security testing and monitoring.
- Enhanced mobile-first passenger experience.

## 🎯 Project Objective

The objective of CloudBus is to demonstrate how cloud-oriented application design, backend development, database management, authentication, and digital verification can be combined into a practical transportation management solution.

This project was developed as part of the **CodeAlpha Cloud Computing Internship — Task 3**.

## 👨‍💻 Developer

**Abdullah Rashid**

Cybersecurity Enthusiast | VAPT | Security Research | Python Development

<p>
  <a href="https://github.com/rashidabdullah5737-ai">GitHub</a> •
  <a href="https://linkedin.com/in/abdullah-rashid-a1554b388">LinkedIn</a> •
  <a href="https://rashidabdullah5737-ai.github.io">Portfolio</a>
</p>

---

<p align="center">
  <strong>CloudBus — Making Bus Pass Management Smarter, Simpler & More Secure.</strong>
  <br/>
  ⭐ If you find this project interesting, consider giving the repository a star!
</p>
