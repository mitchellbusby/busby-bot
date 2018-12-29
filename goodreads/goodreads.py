import os
import requests
import xmltodict
from random import shuffle

API_URL = os.environ.get('GOODREADS_URL') 

def book_to_string(book):
    title = book['title']
    author = book['authors']['author']['name']
    return f"You should read '{title}' by {author}"

def get_random_book_from_shelf():
    response = requests.get(API_URL)
    dictionary_response = xmltodict.parse(response.text)

    reviews = dictionary_response['GoodreadsResponse']['reviews']['review']

    # Shuffle the list
    shuffle(reviews)

    return book_to_string(reviews[0]['book'])