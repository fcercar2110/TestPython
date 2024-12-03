import random
import string

def generate_palindrome(count=5, length=5):
    """Genera una lista de cadenas que son palíndromos."""
    palindrome = []
    for _ in range(count):
        # Generar la primera mitad del palíndromo
        half = ''.join(random.choices(string.ascii_letters, k=length // 2))
        if length % 2 == 0:
            # Construir el palíndromo si la longitud es par
            palin = half + half[::-1]
        else:
            # Construir el palíndromo si la longitud es impar
            palin = half + random.choice(string.ascii_letters) + half[::-1]
        palindrome.append(palin)
    return palindrome

def generate_non_palindrome(count=5, length=5):
    """Genera una lista de cadenas que no son palíndromos."""
    non_palindrome = []
    while len(non_palindrome) < count:
        # Generar una cadena aleatoria
        rand_str = ''.join(random.choices(string.ascii_letters, k=length))
        if rand_str != rand_str[::-1]:  # Solo agregar si no es un palíndromo
            non_palindrome.append(rand_str)
    return non_palindrome
