import unittest

from .matchers import matches_library_query, matches_greeting

class LibraryMatcherTests(unittest.TestCase):
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

class GreetingMatcherTests(unittest.TestCase):
    def test_should_match_gday(self):
        s = 'g\'day'

        result = matches_greeting(s)

        self.assertTrue(result)

    def test_should_match_hi(self):
        s = 'hi there'
        
        result = matches_greeting(s)

        self.assertTrue(result)


if __name__ == "__main__":
    unittest.main()