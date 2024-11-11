from contants import GOOGLE_BOOKS_API_KEY, GOOGLE_API_URL
import requests

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
