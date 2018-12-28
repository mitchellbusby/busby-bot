from goodreads import client
import requests
import xmltodict
import os

API_URL = os.environ.get('GOODREADS_URL') 

def get_random_book_from_shelf():
    response = requests.get(API_URL)
    dictionary_response = xmltodict.parse(response.content)
    return dictionary_response['GoodreadsResponse']['reviews'][0]