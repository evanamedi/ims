# Inventory Management System (IMS)

## Overview

This Inventory Management System is a web-based application designed to manage various aspects of inventory operations, including suppliers, products, customers, orders, and sales. The application is built using the Flask web framework and follows a modular structure to maintain separation of concerns and enhance scalability. The system leverages RESTful APIs to handle CRUD operations and supports real-time data interaction (MySql) through a dynamic front-end interface.

## Improvements

Refactorization to the database operation logic is necessary to maintain scalability. Within archive/logic/database_logic.py there exists a class called "Table" that was used in the first version of the application to minimize code duplication, but was abandoned for Flask Alchemy. The intent was to use a modern framework for handling database operations, and not relying on the previous logic that was created manually. The intent was good, but the execution was poor.

## Features

-   **Dashboard:** A central location to monitor key metrics and activities.
-   **Suppliers Management:** Create, update, retrieve, and delete supplier information.
-   **Products Management:** Manage products, including linking them to suppliers and tracking inventory levels.
-   **Customers Management:** Handle customer details and their related orders and sales.
-   **Orders and Sales:** Manage orders and sales, linking them to customers and products.
-   **Analytics:** View and analyze data through the integrated analytics dashboard.

## Project Structure

-   **`app.py`**: The main application entry point.
-   **`api_routes.py`**: Contains the blueprint and API resource mappings.
-   **`models.py`**: Defines the database models for the application.
-   **`database_operations.py`**: Utility functions for performing database operations.
-   **`templates/`**: HTML templates for dynamically rendering the UI.
-   **`api_v3_resources/`**: Contains the API resource classes for handling CRUD operations.

## API Endpoints

-   **Suppliers:**

    -   `POST /api/v3/suppliers/create`
    -   `GET /api/v3/suppliers/<id>`
    -   `PUT /api/v3/suppliers/<id>`
    -   `DELETE /api/v3/suppliers/<id>`

-   **Products:**

    -   `POST /api/v3/products/create`
    -   `GET /api/v3/products/<id>`
    -   `PUT /api/v3/products/<id>`
    -   `DELETE /api/v3/products/<id>`

-   **Customers:**

    -   `POST /api/v3/customers/create`
    -   `GET /api/v3/customers/<id>`
    -   `PUT /api/v3/customers/<id>`
    -   `DELETE /api/v3/customers/<id>`

-   **Orders:**

    -   `POST /api/v3/orders/create`
    -   `GET /api/v3/orders/<id>`
    -   `PUT /api/v3/orders/<id>`
    -   `DELETE /api/v3/orders/<id>`

-   **Sales:**
    -   `POST /api/v3/sales/create`
    -   `GET /api/v3/sales/<id>`
    -   `PUT /api/v3/sales/<id>`
    -   `DELETE /api/v3/sales/<id>`

#### Additional Notes

This project was created with the intent of testing different tools and technologies, and as such contains dependencies that may not be currently used, but exist in use within the archives. There is also several instances of the same logic implemented in many different ways- again usually archived if/when abandoned.
