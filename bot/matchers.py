import re

apostrophe_regex = "[‘'’]"

def matches_library_query(text):
    return re.search('is ' + apostrophe_regex + '(.*?)' + apostrophe_regex + ' available at the library', text)