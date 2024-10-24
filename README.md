                                                   Inventory Management System

Overview

The Inventory Management System is designed to streamline the management of products, suppliers, and sales for an organization. It provides two types of users: Admin and Employee. The system includes a billing page, employee and supplier details, product management, sales tracking, and a "Forgot Password" feature that utilizes email functionality for password recovery.



Features

1. User Roles

Admin:

Manage employee details.
Manage supplier details.
Add, update, and delete product details.
View sales reports and statistics.

Employee:

Access billing page.
Manage product sales.

2. Billing Page

Employee can generate bills for customers.
Includes product selection, customer details input, and real-time billing calculations (e.g., discounts, taxes).

3. Employee and Supplier Management

Admin can add, edit, and delete employee details.
Admin can manage supplier details, ensuring product availability.

4. Product Management

Admin can add, edit, and delete product information.
Each product has attributes such as price, quantity, category, etc.

5. Sales Management

Admin can view daily, weekly, or monthly sales reports.
Tracks products sold, revenue generated, and profit margins.

6. Forgot Password Functionality

Users can reset their password through email.
A recovery email is sent with a link to reset the password.


Tech Stack
Frontend: HTML, CSS, JavaScript, Bootstrap
Backend: Python (Flask)
Database: SQLite
Email Service: SMTP for email functionality


Installation Instructions

Clone the repository:

git clone https://github.com/SandeshGharal264/Inventory-Management-System.git

Navigate to the project directory:

cd Inventory-Management-System

Install dependencies:

pip install -r requirements.txt

Set up the SQLite database:

flask db upgrade

Run the Flask application:

flask run

Access the system at http://localhost:5000.


How to Use
Admin: Login with admin credentials to manage employees, suppliers, and products.
Employee: Login to the system to handle billing for customers.


Future Enhancements

Add advanced sales analytics.

Integrate barcoding for product management.

Add support for multiple languages.
