import re

def matches_library_query(text):
    return re.search('is \'(.*?)\' available at the library', text)