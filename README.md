 Tyrant – Rental & Property Management System

Tyrant is a rental and property management system built with Django and Django REST Framework (DRF).
The platform helps users find houses or apartments to stay in while enabling landlords to market and manage their rental properties.

The system exposes RESTful APIs that can be consumed by a web or mobile frontend and is designed to be easily extended and maintained.

 Features

Property and apartment listings

Booking and reservation management

User authentication and role support (tenants, landlords, admins)

Wallet system for managing balances and transactions

User verification services

RESTful API architecture for easy integration

 Tech Stack

Backend: Python, Django, Django REST Framework

Database: PostgreSQL

Authentication: Django authentication / DRF-based auth

Deployment Ready: Procfile included (e.g. Heroku)

 Project Structure
├── bookings/           # Booking logic and APIs
├── properties/         # Property and apartment management
├── users/              # User accounts and authentication
├── wallet/             # Wallet and transaction handling
├── verification/       # User verification services
├── tyrent_backend/     # Django project configuration
├── manage.py           # Django management entry point
├── Procfile            # Deployment configuration
├── requirements.txt    # Project dependencies
├── runtime.txt         # Python runtime version

 Installation & Setup
Prerequisites

Python 3.10+

PostgreSQL

Virtual environment (venv)

Clone the Repository
git clone https://github.com/ivyadisa/tyrant.git
cd tyrant

Create Virtual Environment
python -m venv venv
source venv/bin/activate   # Linux / macOS
venv\Scripts\activate      # Windows

Install Dependencies
pip install -r requirements.txt

Database Configuration

Update the database settings in tyrent_backend/settings.py:

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'tyrant_db',
        'USER': 'your_db_user',
        'PASSWORD': 'your_db_password',
        'HOST': 'localhost',
        'PORT': 5432,
    }
}

Run Migrations
python manage.py makemigrations
python manage.py migrate

Create Superuser
python manage.py createsuperuser

Run the Server
python manage.py runserver

🔗 API Usage

The system exposes REST APIs for:

Properties

Bookings

Users

Wallet operations

Verification services

These APIs can be integrated with a frontend (React, Flutter, etc.) or mobile application.

 Contributing

Contributions are welcome.
Please fork the repository, create a feature branch, and submit a pull request with clear descriptions.

 Future Improvements

Frontend web and mobile applications

Advanced role-based permissions

Email and notification services

Payment gateway integration

 License

This project is open-source and available for further development and customization.