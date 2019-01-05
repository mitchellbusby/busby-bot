import re

def matches_library_query(text):
    return re.match('is \'(.*?)\' available at the library', text)