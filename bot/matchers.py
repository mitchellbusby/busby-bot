import re

apostrophe_regex = "[‘'’]"

def matches_library_query(text):
    return re.search('is ' + apostrophe_regex + '(?P<book_title>.*?)' + apostrophe_regex + ' available at the library', text)

def matches_greeting(text):
    return re.match('hi|hello|g\'day|gday|hola', text) != None

def matches_get_me_the_emoji(text):
    return re.search('get me the emoji for (?P<emoji_query>.*)', text)