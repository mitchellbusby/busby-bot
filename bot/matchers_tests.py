import unittest

from .matchers import matches_library_query

class MatchersTests(unittest.TestCase):
    def test_should_match_simple_query(self):
        s = "@busby_bot is 'the fault in our stars' available at the library"

        result = matches_library_query(s)

        self.assertIsNotNone(result)

        title = result.group('book_title')
        
        self.assertEqual('the fault in our stars', title)

    def test_should_match_annoying_apostrophes(self):
        s = "<@uf3gkblcb> is ‘atlas shrugged’ available at the library"
        
        result = matches_library_query(s)
        
        self.assertIsNotNone(result)

        title = result.group('book_title')

        self.assertEqual('atlas shrugged', title)

if __name__ == "__main__":
    unittest.main()