import requests
import xmltodict
import os

API_URL = os.environ.get('GOODREADS_URL') 

def get_random_book_from_shelf():
    response = requests.get(API_URL)
    dictionary_response = xmltodict.parse(response.text)
    # print(dictionary_response['GoodreadsResponse'].keys())
    # print(dictionary_response['GoodreadsResponse']['reviews'])

    reviews = dictionary_response['GoodreadsResponse']['reviews']
    
    thing = ''

    for key, value in reviews:
        thing = f'{key}, {value}'

    return thing