def user_input():
    frase = input("Ingrese una frase: ")
    # VALIDAR QUE LA FRASE NO ESTÉ VACÍA
    frase = frase.lower()
    while not frase.strip():
        print("La frase no puede estar vacía. Por favor, intente de nuevo.")
        frase = input("Ingrese una frase: ")
    return frase

def contar_vocales():
    frase = user_input()
    vocales = "aeiou"
    consonantes = "bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ"
    contador = sum(1 for char in frase if char in vocales)
    contador2 = sum(2 for char in frase if char in consonantes)
    
    
    print(f"La cantidad de vocales en la frase es: {contador}")
    print(f"El doble de la cantidad de consonantes en la frase es: {contador2}")




if __name__ == "__main__":
    contar_vocales()# Contador de vocales en una frase ingresada por el usuario
    