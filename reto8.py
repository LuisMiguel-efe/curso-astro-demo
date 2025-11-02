# Ordenador de nombres
"""Descripcion: Pide al usuario una lista de nombres separados por comas y los ordena alfabéticamente.
Mostrando tamvien cuantos nombres empiezan por cada letra del alfabeto.
Objetivo del reto: Practicar el uso de listas, diccionarios y funciones en Python"""

def ordenar_nombres(nombres):
    lista_nombres = [nombre.strip() for nombre in nombres.split(",")]
    lista_nombres.sort()
    conteo_letras = {}
    for nombre in lista_nombres:
        primera_letra = nombre[0].upper()
        if primera_letra in conteo_letras:
            conteo_letras[primera_letra] += 1
        else:
            conteo_letras[primera_letra] = 1
            
    print("Nombres ordenados:")
    for nombre in lista_nombres:
        print(f" - {nombre}")
    print("\nConteo de nombres por letra inicial:")
    for letra, conteo in sorted(conteo_letras.items()):
        print(f" {letra}: {conteo}")
        
if __name__ == "__main__":
    entrada = input("Ingrese una lista de nombres separados por comas: ")
    ordenar_nombres(entrada)
    