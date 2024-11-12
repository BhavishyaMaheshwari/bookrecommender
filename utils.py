from contants import GOOGLE_BOOKS_API_KEY, GOOGLE_API_URL, ALLOWED_EXTENSIONS
import requests
import random
import string
import pickle
import re

def searchBooks(query):
    params = {
        'q': query,
        'key': GOOGLE_BOOKS_API_KEY,
        'maxResults': 30,
    }
    response = requests.get(GOOGLE_API_URL, params=params)
    return response.json()

def searchBookById(book_id):
    response = requests.get(GOOGLE_API_URL + f'/{book_id}')
    return response.json()

def get_authors(authors):
    return ', '.join(authors) or "No Author Found"

def get_desc(description):
    if (description): return description[:150] + "..."
    else:
        return "No Description"
    
def get_image(volume):
    image = volume.get('imageLinks', {})
    
    # book['volumeInfo']['imageLinks']['smallThumbnail'] or '/static/img-nf.png'
    return image.get('smallThumbnail', '/static/img-nf.png')  

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

def generate_random_id():
    prefix = random.choice(string.ascii_lowercase) + "_"
    random_part =  ''.join(random.choices(string.ascii_letters + string.digits, k=10))
    return prefix + random_part

def addNewBook(data):
    file = open("book.dat",'ab')
    pickle.dump(data,file)
    file.close()

def searchCustomBookById(book_id):
    file = open("book.dat",'rb')
    while True:
       try:
            rec= pickle.load(file)
            if rec['id'] == book_id:
                return rec
       except Exception:
          break
    file.close()
    return None

def searchCustomBookByQuery(query):
    file = open("book.dat",'rb')
    while True:
       try:
            rec= pickle.load(file)
            if advanced_search(query, rec['volumeInfo']['title']):
                return rec
       except Exception:
          break
    file.close()
    return None


def advanced_search(substring, string, case_sensitive=False, whole_word=False):
    # Build the regex pattern based on options
    pattern = re.escape(substring)  # Escape special characters in the substring
    
    if whole_word:
        # Use \b to indicate word boundaries
        pattern = r'\b' + pattern + r'\b'
    
    # Compile the regex pattern with the appropriate flags
    flags = 0 if case_sensitive else re.IGNORECASE
    regex = re.compile(pattern, flags)
    
    # Search for the pattern in the string
    match = regex.search(string)
    return match is not None  # Returns True if a match is found, False otherwise
