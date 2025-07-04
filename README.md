# Expense Tracker API

A Django REST Framework-based API that allows users to track personal income and expenses. The API supports user registration, JWT authentication, role-based access control, and automated tax calculation for debit transactions.

---
## API Documentation
You can find the full API reference including sample requests and responses here:

Postman Docs: https://documenter.getpostman.com/view/44472081/2sB34bMjMa


## Features

-  JWT Authentication (`djangorestframework-simplejwt`)
-  User registration and login
-  Create, retrieve, update, and delete expense records
-  Superuser can access all data; regular users can only access their own
-  Automatic tax calculation on debit transactions (10%)
-  Role-based access control with custom permissions
-  RESTful endpoints with proper HTTP status codes
-  API testing using Postman

---

## Getting Started

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/expense-tracker-api.git
```
## Set Up Virtual Environment
```bash
python -m venv venv
source venv/bin/activate
```
## Install Requirements
```bash
pip install -r requirements.txt
```
## Apply Database Migrations
```bash
python manage.py migrate
```
### 5. Create Superuser

```bash
python manage.py createsuperuser
python manage.py runserver
```
The API will be available at http://127.0.0.1:8000/.
