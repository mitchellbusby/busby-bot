import re
from goodreads import get_random_book_from_shelf
from library import is_book_available
from .matchers import matches_library_query, matches_greeting

STATES = {
    'NOTHING': 'NOTHING',
    'REQUESTED_BOOK': 'REQUESTED_BOOK'
}

def reset_ctx(ctx):
    ctx = {}

# Grok and respond
def handle_message(text, reply_func, state, context):
    text = text.lower()
    print(text)
    if 'i want a book' in text or 'give me a book' in text:
        reset_ctx(context)
        reply_func(get_random_book_from_shelf())
    elif 'is it available at the library' in text:
        reply_func('Sorry, I don\'t know how to tell you that yet.')
    elif matches_library_query(text) != None:
        match_result = matches_library_query(text)
        book_title = match_result.group('book_title')
        print(book_title)
        book_available = is_book_available(book_title)
        ## TODO: disambiguate between a book being not available
        ## and the book not being available at the library
        if book_available:
            reply_func('That book _is_ available.')
        else:
            reply_func('That book is _not_ available.')
    elif state == STATES["REQUESTED_BOOK"]:
        reply_func('Sorry - ask me to give you a book!')
    elif matches_greeting(text):
        reply_func('G\'day! Ask me to give you a book!')
    else:
        reply_func('Not sure what you meant. Ask me to give you a book!')