import re
import get_random_book_from_shelf from goodreads

# Grok and respond
def handle_message(text, reply_func):
    print(text)

    if 'I want a book' in text:
        reply_func(get_random_book_from_shelf())

    reply_func('gudday')