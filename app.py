from flask import Flask, request, jsonify, render_template
import requests
from dotenv import load_dotenv
import os

# Load environment variables from .env
load_dotenv()

# Initialize Flask app
app = Flask(__name__)
GOOGLE_BOOKS_API_KEY = os.getenv("GOOGLE_BOOKS_API_KEY")

# A simple in-memory data structure to store user likes and favorites
user_data = {
    "likes": set(),
    "favorites": set()
}

# Helper function to search books using Google Books API
def search_books(query):
    url = "https://www.googleapis.com/books/v1/volumes"
    params = {
        'q': query,
        'key': GOOGLE_BOOKS_API_KEY,
        'maxResults': 5
    }
    response = requests.get(url, params=params)
    return response.json()

# Route for the home page
@app.route('/')
def home():
    return render_template('index.html')

# Route for searching books
@app.route('/search', methods=['GET'])
def search():
    query = request.args.get('query')
    results = search_books(query)

    # Add liked and favorite status to each book
    for item in results.get('items', []):
        book_id = item['id']
        item['liked'] = book_id in user_data['likes']
        item['favorite'] = book_id in user_data['favorites']

    return jsonify(results)

# Route for liking a book
@app.route('/like', methods=['POST'])
def like_book():
    book_id = request.json['book_id']
    user_data['likes'].add(book_id)
    return jsonify({"message": "Book liked!", "likes": list(user_data['likes'])})

# Route for marking a book as favorite
@app.route('/favorite', methods=['POST'])
def favorite_book():
    book_id = request.json['book_id']
    user_data['favorites'].add(book_id)
    return jsonify({"message": "Book added to favorites!", "favorites": list(user_data['favorites'])})

# Route for viewing liked books
@app.route('/liked_books', methods=['GET'])
def liked_books():
    liked_books_data = []
    for book_id in user_data['likes']:
        book_data = search_books(book_id)  # Make sure to use the right ID for search
        if 'items' in book_data:
            liked_books_data.append(book_data['items'][0])  # Add the first item if found
    return jsonify({"liked_books": liked_books_data})

@app.route('/favorite_books', methods=['GET'])
def favorite_books():
    favorite_books_data = []
    for book_id in user_data['favorites']:
        book_data = search_books(book_id)  # Make sure to use the right ID for search
        if 'items' in book_data:
            favorite_books_data.append(book_data['items'][0])  # Add the first item if found
    return jsonify({"favorite_books": favorite_books_data})

# Run the app
if __name__ == "__main__":
    app.run(debug=True)
