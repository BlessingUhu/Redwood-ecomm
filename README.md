# Redwood Ecommerce Web Application

Redwood is a full-fledged ecommerce web application built using Django Framework, including SQL, Python, HTML, and SCSS. It provides a platform for users to 
browse, search, and purchase products online. This README provides an overview of the application and instructions for setting it up 
and running it locally.

## Features
- User registration and authentication
- Product catalog with search and filtering options
- Shopping cart functionality
- Order history
- Admin dashboard for managing, orders, and users

### Technologies Used
1. SQL (Structured Query Language): Used to create and manage the database that stores product information, user data, and order details.
2. Python: The backend of the application is built using Python, utilizing frameworks such as Flask or Django for routing, handling requests, and managing the business logic.
3. HTML (Hypertext Markup Language): Responsible for the structure and layout of the web pages.
SCSS (Sassy CSS): Used to enhance the styling capabilities of CSS and make the code more maintainable.
4. JavaScript: Enables interactive features and dynamic behavior on the client-side.
Payment Gateway Integration: Integration with a payment gateway API to securely process customer payments.

#### Setup Instructions

Clone the repository:
git clone [https://github.com/your-username/redwood.git](https://github.com/BlessingUhu/Redwood-ecomm.git)

Create a virtual environment and activate it:
python3 -m venv redwood-env
source redwood-env/bin/activate

Install the required Python dependencies:
pip install -r requirements.txt

Set up the database:
Create a SQL database using your preferred method.
Update the database connection configuration in config.py or a similar configuration file.

Apply database migrations:
python manage.py db migrate
python manage.py db upgrade


Run the application:
python manage.py runserver
Open your web browser and visit http://localhost:8000 to access the Redwood application.

# Folder Structure
1. redwood_app: Contains the main application logic.
2. models: Defines the database models.
3. views: Implements the views and controllers for different pages and functionalities.
4. templates: Contains HTML templates for rendering the views.
5. static: Includes CSS, JavaScript, and other static files.
6. migrations: Manages database migrations using django migration.
7. config.py: Configuration file for the application.
8. requirements.txt: Lists the Python dependencies required for the application.
9. manage.py: Entry point for running management commands (e.g., running the server, applying database migrations).
