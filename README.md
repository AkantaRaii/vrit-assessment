# Expense Tracker API

A Django REST Framework-based API that allows users to track personal income and expenses. The API supports user registration, JWT authentication, role-based access control, and automated tax calculation for debit transactions.

---

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

