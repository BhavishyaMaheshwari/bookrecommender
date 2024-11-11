from flask import Flask, request, jsonify, render_template, request
from dotenv import load_dotenv
import os
from utils import searchBooks, searchBookById

# Load environment variables from .env
load_dotenv()

# Initialize Flask app
app = Flask(__name__)

# Route for the home page
@app.route('/')
def home():
    return render_template('index.html')

# Route for searching books
@app.route('/search', methods=['GET'])
def search():
    query = request.args.get('query')
    results = searchBooks(query)
    return jsonify(results)

# Route for searching books by their id
@app.route('/booksById', methods=['POST'])
def favorites():
    ids = request.get_json()['ids']
    result = []
    for id in ids:
        book= searchBookById(id)
        result+=[book]
    return jsonify(result)

@app.after_request
def after_request(response):
    response.headers["Cache-Control"] = "no-store, max-age=0"
    return response


# Run the app
if __name__ == "__main__":
    app.run(debug=True)
