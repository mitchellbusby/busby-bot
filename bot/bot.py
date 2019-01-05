import re

# Grok and respond
def handle_message(text, reply_func):
    print(text)
    reply_func('gudday')