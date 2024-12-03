"""
    palindrome.py -> Se llama desde main.py

    Código que contiene las funciones relacionadas con la
    verificación de cadenas palíndromas, incluyendo la
    normalización de caracteres y la lógica de comparación. 

        Ultima Modificación. 02/12/2024
        Autor. Gregorio Coronado Morón
        Modificado por. Fernando Cervera Carrera
        Dependencias. Unicodedata

"""

import unicodedata

def normalize(string):
    """Elimina tildes y normaliza caracteres Unicode."""
    return ''.join(
        char for char in unicodedata.normalize('NFD', string)
        if unicodedata.category(char) != 'Mn'
    )

def is_palindrome(string):
    """
    Verifica si una cadena es un palíndromo.
    Ignora espacios, mayúsculas, tildes y caracteres no alfanuméricos.
    """

    # Verificar que la entrada sea una cadena
    if not isinstance(string, str):
        raise TypeError("La entrada debe ser una cadena de texto.")
    

    # Verificar si la cadena está vacía o tiene solo espacios
    if not string.strip():  # strip() elimina los espacios al principio y al final
        return "La cadena no puede estar vacía o contener solo espacios."


    # Normalizar la cadena (eliminar tildes y convertir a minúsculas)
    string = normalize(string).lower()

    # Eliminar caracteres no alfanuméricos
    clean_str = ''.join(char for char in string if char.isalnum())

    # Comparar la cadena limpia con su reverso
    return clean_str == clean_str[::-1]
