import unittest

from .matchers import matches_library_query

class MatchersTests(unittest.TestCase):
    def test_should_match_simple_query(self):
        s = "@busby_bot is 'atlas shrugged' available at the library"

        result = matches_library_query(s)

        self.assertIsNotNone(result)

    def test_should_match_annoying_apostrophes(self):
        s = "<@uf3gkblcb> is ‘atlas shrugged’ available at the library"
        
        result = matches_library_query(s)
        
        self.assertIsNotNone(result)

if __name__ == "__main__":
    unittest.main()