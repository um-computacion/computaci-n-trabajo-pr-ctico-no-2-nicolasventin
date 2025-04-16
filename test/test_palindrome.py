import unittest
from palindrome import is_palindrome  # Asegurate de importar la función después

class TestPalindromosSimples(unittest.TestCase):
    def test_oso(self):
        self.assertTrue(is_palindrome("oso"))

    def test_reconocer(self):
        self.assertTrue(is_palindrome("reconocer"))

    def test_radar(self):
        self.assertTrue(is_palindrome("radar"))

if __name__ == '__main__':
    unittest.main()
