"""
    Programa principal que gestiona la interacción con el usuario.
    Contiene un bucle infinito que solicita al usuario frases por teclado 
    y determina si son palíndromas hasta que se escriba la palabra "salir". 

        Ultima Modificación. 2/12/2024
        Autor. Fernando Cervera Carrera
        Dependencias. is_palindrome

"""


from app.scripts.palindrome import is_palindrome

def main():
    loop = True

    while loop:

        phrase = input("Introduce una frase (o escribe 'salir' para terminar): ")

        if phrase.lower() == "salir":
            print("Programa finalizado.")
            loop = False
        else:
            try:
                # Comprobar si es palíndromo
                result = is_palindrome(phrase)
                
                if result == True:
                    print("La frase es palíndroma")
                elif result == False:
                    print("La frase NO es palíndroma")
                else:
                    # En caso que devuelva un mensaje de error, por ejemplo, la cadena esta vacía.
                    print(result)
            except TypeError as e:
                # Controlar el TypeError si la función recibe un tipo incorrecto
                print(f"Error: {e}. Por favor, introduce una cadena de texto válida.")
            except Exception as e:
                # Capturar cualquier otro error inesperado
                print("Por favor, inténtalo nuevamente.")

