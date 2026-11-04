# 🚌 CloudBus — Cloud-Based Bus Pass Management System

A web-based bus pass and ticket booking application developed using Python Flask and SQLite, featuring passenger authentication, route browsing, seat booking, QR-code ticket generation, and staff-based ticket verification.

**Internship:** CodeAlpha Cloud Computing Internship — Task 3  
**Developer:** Abdullah Rashid  
**Domain:** Cloud Computing

## 🚀 Project Overview

CloudBus simplifies the bus ticket booking and verification process through a centralized web application.

Passengers can register, log in, browse routes, reserve seats, and access QR-code-based tickets. Authorized staff can scan QR codes and verify passenger tickets.

## ✨ Key Features

### Passenger Features
- User registration and login
- Secure password hashing
- Browse available bus routes
- Book bus seats
- Unique ticket ID generation
- QR-code ticket generation
- Personal booking history
- Personal ticket verification

### Staff Features
- Dedicated staff role
- Staff-only QR scanner
- Verify tickets belonging to other passengers
- Restricted access to staff functionality

### Security Features
- Werkzeug password hashing
- Flask-Login authentication
- Role-based access control
- Passenger ticket ownership protection
- Database-level duplicate seat prevention
- Unique ticket identifiers
- Server-side booking validation

## 🛠️ Technologies

- Python
- Flask
- Flask-SQLAlchemy
- SQLite
- Flask-Login
- Werkzeug
- HTML5, CSS3 and JavaScript
- QR Code
- html5-qrcode
- Kali Linux
- Git and GitHub

## 🏗️ Project Structure

```text
Cloud-Based-Bus-Pass-System/
├── app.py
├── models.py
├── config.py
├── requirements.txt
├── .env.example
├── .gitignore
├── README.md
├── templates/
│   ├── index.html
│   ├── login.html
│   ├── register.html
│   ├── routes.html
│   ├── bookings.html
│   ├── verify.html
│   └── scanner.html
└── static/
    ├── css/
    ├── js/
    ├── images/
    └── qrcodes/
