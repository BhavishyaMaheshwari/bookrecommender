import os

GOOGLE_BOOKS_API_KEY = os.getenv("GOOGLE_BOOKS_API_KEY")
GOOGLE_API_URL = "https://www.googleapis.com/books/v1/volumes"
UPLOAD_FOLDER = './static/books_images'
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg'}
