# System of Ratings and Reviews

This is a Django-based project designed to manage ratings and reviews for different entities, such as products, services, or businesses. It provides functionality to create, view, update, and delete ratings and reviews. The system also allows users to rate items and leave feedback in a structured way.

## Features

- **User Authentication:** Users can sign up, log in, and manage their profiles.
- **Review System:** Users can leave detailed reviews with text feedback.
- **Admin Panel:** Admins can manage ratings, reviews, and users through the Django admin interface.
- **JWT Authentication:** API endpoints are protected by JWT tokens for secure access.

## Requirements

- Python 3.x
- Django 4.x
- Django REST Framework
- PostgreSQL (or any other supported database)
- Docker (for containerized deployment)

## Installation

To run this project locally or in a Docker container, follow these steps:

### 1. Clone the Repository

```bash
git clone https://github.com/Nestorkoo/system-of-ratings-and-reviews.git
cd system-of-ratings-and-reviews
```
### 2. Set up the Environment

If you're not using Docker, create a virtual environment and install dependencies:
```bash
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt`
```
### 3. Set Up the Database

If you're using PostgreSQL, ensure your database is running, and create the necessary tables by running the following command:

bash

Copy code
```bash
python manage.py migrate
```
Alternatively, you can configure your preferred database by adjusting the settings in `settings.py`.

### 4. Run the Development Server

To start the Django development server:

bash

Copy code
```bash
python manage.py runserver 
```
By default, the server will run on `http://127.0.0.1:8000/`.

## API Endpoints

### Authentication

-   **POST** `/api/v1/login/` – Login with JWT Authentication.
-   **POST** `/api/v1/register/` – Register a new user.
-   **GET** `/api/v1/pforile/<str:username>/` – Register a new user.

### Ratings and Reviews


-   **GET** `/api/v1/reviews` – List all reviews.
-   **POST** `/api/v1/create` – Create a new review.
-   **PUT** `/api/v1/delete/{id}/` – Update a review.
-   **DELETE** `/api/v1/statistic/{company}/` – Delete a review.


