# Rotten Tomatoes Web App

This is a web application inspired by Rotten Tomatoes, built using Django. It allows users to browse movies, view details about each movie, and rate/review them.

## Features

- Browse Movies: Users can browse through a collection of movies fetched from the database.
- Movie Details: Detailed information about each movie, including synopsis, release date, cast, and crew.
- User Authentication: Users can sign up, log in, and log out.
- User Reviews & Ratings: Authenticated users can leave reviews and ratings for movies.
- Search Functionality: Users can search for movies by title.
- Responsive Design: The application is designed to work well on both desktop and mobile devices.

## Installation
1. Clone Repository:
```sh
    git clone -b master https://gitlab.com/sfaas1/knockoff-of-rotten-tomatoes.git
```
2. Create and activate virtual environment in same folder where you clone a repository:
```sh
    python3 -m venv <yourVENV>
    or:
    python -m venv <yourVENV>
```
```sh
    win: <yourVENV>\Scripts\activate
    or: source <yourVENV>\Scripts\activate   
    macOS/linux: source <yourVENV>/bin/activate
```
3. Navigate to Directory:
```sh
    cd knockoff-of-rotten-tomatoes
```
4. Install Dependencies:
```sh
    pip install -r req.txt
```
5. Database Setup:
- Create a new database for the application or use our.
6. Run Migrations:
```sh
    python manage.py migrate
```
7. Create Superuser:
```sh
    python manage.py createsuperuser
```
8. Run Server:
```sh
    python manage.py runserver
```
9. Access Application:
- Open a web browser and navigate to http://127.0.0.1:8000/ to access the application.

## Usage

- Home Page: Browse through the list of movies, search for specific titles.
- Movie Detail Page: Click on a movie to view its details, including synopsis, cast, crew, and user reviews.
- Authentication: Sign up for a new account or log in with existing credentials to leave reviews and ratings.
- Admin Panel: Access the admin panel at http://127.0.0.1:8000/admin/ to manage movies, users, and reviews.
