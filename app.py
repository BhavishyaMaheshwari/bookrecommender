from flask import Flask, request, jsonify, render_template, request, flash, redirect
from werkzeug.utils import secure_filename
from dotenv import load_dotenv
import os
from utils import *
from contants import UPLOAD_FOLDER
import time

# Load environment variables from .env
load_dotenv()

# Initialize Flask app
app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# Route for the home page
@app.route('/')
def home():
    return render_template('home.html')

# Route for searching books
@app.route('/search', methods=['GET'])
def search():
    query =  request.args.get('query') 
    results = searchBooks(query)
    custom_books = searchCustomBookByQuery(query)
    if (custom_books):
        results['items'] = results['items'] + [custom_books]
    return render_template('search.html', books=results, search_query=query)

# Route for searching books by their id
@app.route('/booksById', methods=['POST'])
def booksById():
    ids = request.get_json()['ids']
    result = []
    for id in ids:
        book = searchCustomBookById(id)
        if (not book):
            book= searchBookById(id)
        result+=[book]
    return jsonify(result)

@app.route('/add-book', methods=['GET','POST'])
def addBook():
    if request.method == 'POST':
        title = request.form.get('title')
        authors = request.form.get('authors')
        categories = request.form.get('categories')
        description = request.form.get('description')
        links = request.form.get('links')
        cover = None
        
        if 'cover' not in request.files:
            flash('No file part')
            return redirect(request.url)
        file = request.files['cover']
        if file.filename == '':
            flash('No selected file')
            return redirect(request.url)
        if file and allowed_file(file.filename):
            cover = str(time.time()).split('.')[0] + secure_filename(file.filename) 
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], cover))

        book = {
            'volumeInfo': {
                'title': title,
                'authors': authors.split(','),
                'categories': categories.split(','),
                'description': description,
                'infoLink': links,
                'imageLinks': {
                    'smallThumbnail': '/static/books_images/' + cover
                }
            },
            'id': generate_random_id(),
            'customBook':True,
            'accessInfo': {
                'webReaderLink': ''
            }
        }
        addNewBook(book)

        # return jsonify(book)
        redirect('/')

    return render_template('add-book.html')

@app.route('/favorites')
def favorites():
    return render_template('favorites.html')

@app.route('/likes')
def likes():
    return render_template('likes.html')

@app.context_processor
def utility_processor():
    return dict(get_authors=get_authors, get_desc=get_desc, get_image=get_image)


# Run the app
if __name__ == "__main__":
    app.run(debug=True)
