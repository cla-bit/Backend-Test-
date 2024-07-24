
# Welcome!

Hi! this your determinant test for the position of Django backend developer at **PayBox360**.  If you have any issues, you can read this docs or also contact Lolu for further clarification.


##  Overview

For this exercise you will be cover some basic concepts of web development and production ready deployment  and you will hence be tested in the following basic concepts.

- Django and Django query-sets
- PostgreSQL Setup and connection to Django
- Cloud deployment
- PEP guidelines, conformity and quality of code 
- General understanding of the python programming language.

## Test Rundown

You will be required to fork this repository into your personal account and then carry out few operations of extending functionality of the application and then make a pull request with your branch name to the main branch as you progress.

## Test Guide

After completing stage the process in in the rundown, please create branch for your self, please make sure to name the the branch with the following convention **\<yourname>/update**, and also all commits to your branch should carry a message in the following format **\<ACTIVITY>[Activity details]**.

- A sample branch name would be **paul/update**, and., 
- A sample commit message would be **FIX[ADDED CORS CONTROL]**

## Task Description

You are required to extend a skeleton application and build it into an inventory management system to such that it can provide the abilities below:


**Project: Simple E-commerce API**

**Requirements:**
1. **User Management:**
   - Implement user registration and login with JWT authentication.
   
2. **Product Management:**
   - Create models for Product and Category.
   - Implement CRUD operations for products (create, read, update, delete).

3. **Order Management:**
   - Create an Order model.
   - Allow users to place orders with multiple products.
   - Implement a basic order history endpoint for users.

**Detailed Instructions:**

1. **Setup:**
   - Create a new Django project.
   - Configure the project with Django REST Framework.
   - Make sure to use PostgreSQL

2. **User Authentication:**
   - Use Django's built-in User model.
   - Implement registration and login endpoints using JWT for authentication.

3. **Product and Category Models:**
   - Create models with appropriate fields (e.g., name, description, price for Product; name for Category).
   - Establish relationships (e.g., a product belongs to a category).
   - Implement endpoints for managing products (list, detail, create, update, delete).

4. **Order Model:**
   - Create an Order model with fields like user (ForeignKey), product (ManyToManyField), quantity, and date.
   - Implement an endpoint for placing orders.
   - Create an endpoint to retrieve the order history for the authenticated user.

5. **Testing:**
   - Write unit tests for each endpoint.

**Evaluation Criteria:**
- Correctness: The implementation should meet the requirements.
- Code Quality: Clean, readable, and maintainable code.
- Use of Django Best Practices: Proper use of Django features and conventions.
- Testing: Quality and coverage of unit tests.

**Bonus:**
- Implement search functionality for products.
- Add pagination to product listing.


## Resources for task

**Finally**
You will be provided with a virtual machine IP address hosted on Digital Ocean please host your project appropriately using NGINX,  GUNICORN and POSTGRESQL (as database). A password for the droplet will be provided.

- Please add your postman link to the above created endpoints for review.
- Also note that you can ignore the Docker and CI/CD instantiations on the application.

### Good luck, as we look forward to working with you at Liberty Assured in building amazing projects and relationships.

## How to run the project:

This project makes use of poetry as a dependency manager. To run the project, ensure you have poetry installed.

1. Run `pipx install poetry`
2. Run `pip install poetry`
3. Clone the repository from GitHub.
4. Run `poetry install --no-root` as this will install the dependencies from pyproject.toml file.
5. Run `poetry shell` to create and activate a virtual environment.
6. Run `python manage.py makemigrations` and `python manage.py migrate` to run migrations and migrate command to database.
7. Run `python manage.py runserver` to start the virtual environment to run the application.
8. Install and configure `Postman` to test the endpoints.
9. To exit virtual environment, run `exit` command.

### Note: Ensure you already have set up PostgreSQL database before running migrations and migrate commands.

In case you prefer to use sqlite to make it faster instead of setting up PostgreSQL database,
comment the PostgreSQL `DATABASES settings` section in the `app/settings.py` file and uncomment the
SQLITE3 `DATABASES settings`.

## Environment variables:

Set the following environment variables in your `.env` file. See `.env.example` file for details

```dotenv

SECRET_KEY=YOUR_SECRET_KEY
DEBUG=True# or False for production
DB_NAME=DB_NAME
DB_USER=DB_USER
DB_PASSWORD=DB_PASSWORD
DB_HOST=DB_HOST
DB_PORT=DB_PORT

```

# Run Tests:
Run `pytest app_name/tests` on your terminal

# Postman API Documentation Test Endpoints

1. User management: [Here for the Postman API Documentation](https://backend-test-postman-api.postman.co/workspace/Backend-Test-Postman-API-Worksp~5ac55dbf-f19d-4ded-b830-bf34ccc25755/folder/27786069-cfe5acc1-c99f-4629-8169-9acd63165fab?action=share&creator=27786069&ctx=documentation)
2. Product management: [Here for the Postman API Documentation](https://backend-test-postman-api.postman.co/workspace/Backend-Test-Postman-API-Worksp~5ac55dbf-f19d-4ded-b830-bf34ccc25755/folder/27786069-2a522d0c-68c4-4988-b74f-9011fada2d37?action=share&creator=27786069&ctx=documentation)
3. Order management: [Here for the Postman PI Documentation](https://backend-test-postman-api.postman.co/workspace/Backend-Test-Postman-API-Worksp~5ac55dbf-f19d-4ded-b830-bf34ccc25755/folder/27786069-f67f7517-b9b7-4343-86ab-7c9b76120b3f?action=share&creator=27786069&ctx=documentation)
