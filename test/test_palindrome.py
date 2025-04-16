import unittest
from palindrome import is_palindrome  # Asegurate de importar la función después

class TestPalindromosSimples(unittest.TestCase):
    def test_oso(self):
        self.assertTrue(is_palindrome("oso"))

    def test_reconocer(self):
        self.assertTrue(is_palindrome("reconocer"))

    def test_radar(self):
        self.assertTrue(is_palindrome("radar"))

class TestFrasesPalindromas(unittest.TestCase):

    def test_anita(self):
        self.assertTrue(is_palindrome("Anita lava la tina"))

    def test_mama_roma(self):
        self.assertTrue(is_palindrome("A mamá Roma le aviva el amor a mamá"))

    def test_ruta(self):
        self.assertTrue(is_palindrome("La ruta nos aportó otro paso natural"))

class TestCasosNoPalindromos(unittest.TestCase):

    def test_perro(self):
        self.assertFalse(is_palindrome("perro"))

    def test_hola_mundo(self):
        self.assertFalse(is_palindrome("hola mundo"))

    def test_palabra(self):
        self.assertFalse(is_palindrome("palabra"))

if __name__ == '__main__':
    unittest.main()
