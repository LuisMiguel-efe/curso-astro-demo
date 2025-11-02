"""Reto 9: Registro de estudiantes:
Descripcion:
Crea una clase Estudiante con atributos: nombre, edad, nota.
Luego, permite registrar varios estudiantes y calcular:
El promedio general
El estudiante con mejor nota
"""
class Estudiante:
    def __init__(self, nombre, edad, nota):
        self.nombre = nombre
        self.edad = edad
        self.nota = nota
        
def registrar_estudiantes():
    estudiantes = []
    while True:
        nombre = input("Ingrese el nombre del estudiante (o 'salir' para terminar): ")
        if nombre.lower() == 'salir':
            break
        edad = int(input("Ingrese la edad del estudiante: "))
        nota = float(input("Ingrese la nota del estudiante: "))
        estudiante = Estudiante(nombre, edad, nota)
        estudiantes.append(estudiante)
    return estudiantes
        
def calcular_promedio(estudiantes):
    if not estudiantes:
        return 0
    total_notas = sum(estudiante.nota for estudiante in estudiantes)
    return total_notas / len(estudiantes)

def estudiante_mejor_nota(estudiantes):
    if not estudiantes:
        return None
    return max(estudiantes, key=lambda estudiante: estudiante.nota)

def main():
    estudiantes = registrar_estudiantes()
    promedio = calcular_promedio(estudiantes)
    mejor_estudiante = estudiante_mejor_nota(estudiantes)
    print(f"\nPromedio general de notas: {promedio:.2f}")
    if mejor_estudiante:
        print(f"Estudiante con mejor nota: {mejor_estudiante.nombre} con una nota de {mejor_estudiante.nota:.2f}")
    else:
        print("No se registraron estudiantes.")
        
if __name__ == "__main__":
    main()
    

        
    