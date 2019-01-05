import re
from goodreads import get_random_book_from_shelf

# Grok and respond
def handle_message(text, reply_func):
    print(text)

    if 'I want a book' in text:
        reply_func(get_random_book_from_shelf())
    else:
        reply_func('gudday')