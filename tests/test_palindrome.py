import unittest
from app.scripts.palindrome import is_palindrome
from tests.generate import generate_palindrome, generate_non_palindrome

class TestIsPalindrome(unittest.TestCase):
    def test_palindrome_strings(self):
        palindromic_strs = ["ana", "Amigo, no gima", "Di clases al Cid", "Dábale arroz a la zorra el abad"]  # Lista de cadenas palíndromas
        for s in palindromic_strs:
            result = is_palindrome(s)
            self.assertTrue(
                result,
                f"La cadena '{s}' debería ser un palíndromo, pero la función devolvió {result}."
            )
    
    def test_non_palindrome_strings(self):
        non_palindromic_strs = ["anamaria", "sol", "Fernandito", "The Best", "Palindromo"]  # Lista de cadenas no palíndromas
        for s in non_palindromic_strs:
            result = is_palindrome(s)
            self.assertFalse(
                result,
                 f"La cadena '{s}' NO debería ser un palíndromo, pero la función devolvió {result}."
            )
    
    def test_auto_generated_palindromes(self):
        """Prueba dinámicamente cadenas que son palíndromos."""
        palindromic_strs = generate_palindrome(count=20, length=7)
        for s in palindromic_strs:
            with self.subTest(s=s):  # Subtest para rastrear errores individuales
                result = is_palindrome(s)
                self.assertTrue(
                    result,
                    f"La cadena '{s}' debería ser un palíndromo, pero la función devolvió {result}."
                )

    def test_auto_generated_non_palindromes(self):
        """Prueba dinámicamente cadenas que NO son palíndromos."""
        non_palindromic_strs = generate_non_palindrome(count=10, length=7)
        for s in non_palindromic_strs:
            with self.subTest(s=s):  # Subtest para rastrear errores individuales
                result = is_palindrome(s)
                self.assertFalse(
                    result,
                    f"La cadena '{s}' NO debería ser un palíndromo, pero la función devolvió {result}."
                )

    def test_invalid_type_exceptions(self):
        invalid_inputs = [23, [1, 2, 3], {"key": "value"}, None]  # Entradas de tipos no válidos
        for inp in invalid_inputs:
            with self.subTest(inp=inp):
                with self.assertRaises(TypeError):  # Verifica que se lance la excepción esperada
                    is_palindrome(inp)

if __name__ == "__main__":
    unittest.main()
