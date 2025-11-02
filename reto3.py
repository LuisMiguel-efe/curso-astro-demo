from math import sqrt
"""
🧩 Reto 3: Números Primos (Nivel 3 – Intermedio)

Descripción:
Crea una función es_primo(n) que determine si un número es primo.
Luego, imprime todos los números primos del 1 al 100.    
"""

def es_primo(n):
    # Si es nefativo o 0 o 1 no es primo
    if n <= 1:
        return False
    # Verificar divisibilidad desde 2 hasta la raíz cuadrada del numero
    print(f"raiz cuadrada de {n} mas 1 es {int(sqrt(n))+1}")
    for i in range(2, int(sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True
def imprimir_primos_hasta_100():
    """Imprime todos los números primos del 1 al 100."""
    print("Números primos del 1 al 100:")
    for num in range(1, 101):
        if es_primo(num):
            print(num, end=' ')
    print()  # Nueva línea al final
    
if __name__ == "__main__":
    while True:
        n = int(input("Ingrese un número para verificar si es primo: "))
        if es_primo(n):
            print(f"{n} es un número primo.")
        else:
            print(f"{n} no es un número primo.")
            imprimir_primos_hasta_100()
        if n > 1000:
            break
            
