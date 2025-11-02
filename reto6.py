# Analizador de texto

def analizar_texto(texto):
    palabras = texto.split()
    num_palabras = len(palabras)
    num_caracteres = len(texto)
    palabra_mas_larga = max(palabras, key=len) if palabras else ""
    frecuencia_palabras = {}
    for palabra in palabras:
        palabra = palabra.lower()
        if palabra in frecuencia_palabras:
            frecuencia_palabras[palabra] += 1
        else:
            frecuencia_palabras[palabra] = 1
            
    print(f"Número de palabras: {num_palabras}")
    print(f"Número de caracteres: {num_caracteres}")
    print(f"Palabra más larga: {palabra_mas_larga}")
    print("Frecuencia de palabras:")
    for palabra, frecuencia in frecuencia_palabras.items():
        print(f"  {palabra}: {frecuencia}")

if __name__ == "__main__":
    texto = input("Ingrese un texto para analizar: ")
    analizar_texto(texto)

