import re
from goodreads import get_random_book_from_shelf

STATES = {
    'NOTHING': 'NOTHING',
    'REQUESTED_BOOK': 'REQUESTED_BOOK'
}

def reset_ctx(ctx):
    ctx = {}

# Grok and respond
def handle_message(text, reply_func, state, context):
    text = text.lower()
    if 'i want a book' in text or 'give me a book' in text:
        reset_ctx(context)
        reply_func(get_random_book_from_shelf())
    elif 'is it available at the library' in text:
        reply_func('Sorry, I don\'t know how to tell you that yet.')
    else if state == STATES["REQUESTED_BOOK"]:
        reply_func('Sorry - ask me to give you a book!')
    else:
        reply_func('G\'day! Ask me to give you a book!')