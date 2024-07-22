# FastAPI Netflix Backend


## Author
``` Elijah Ekpen Mensah```
## Overview

This FastAPI project provides a basic backend API for a Netflix-like service with support for managing users, profiles, movies, and subscriptions.

## Setup

1. **Install Dependencies**

    ```bash
    pip install -r requirements.txt
    ```

2. **Run the Application**

    ```bash
    uvicorn main:app --reload
    ```

3. **Access the API**

    Visit `http://localhost:8000` to view the Swagger UI documentation.

## Endpoints

### Users

- `POST /api/users`: Create a new user
- `GET /api/users/{user_id}`: Get user details
- `PUT /api/users/{user_id}`: Update user details
- `DELETE /api/users/{user_id}`: Delete a user

### Profiles

- `POST /api/profiles`: Create a new profile
- `GET /api/profiles/{profile_id}`: Get profile details
- `PUT /api/profiles/{profile_id}`: Update profile details
- `DELETE /api/profiles/{profile_id}`: Delete a profile

### Movies

- `POST /api/movies`: Create a new movie
- `GET /api/movies/{movie_id}`: Get movie details
- `PUT /api/movies/{movie_id}`: Update movie details
- `DELETE /api/movies/{movie_id}`: Delete a movie

### Subscriptions

- `POST /api/subscriptions`: Create a new subscription
- `GET /api/subscriptions/{subscription_id}`: Get subscription details
- `PUT /api/subscriptions/{subscription_id}`: Update subscription details
- `DELETE /api/subscriptions/{subscription_id}`: Delete a subscription

Feel free to expand or modify these endpoints to suit your specific needs.
