"""🧩 Reto 10 – Mini Agenda Persistente (Nivel avanzado – archivos)
Descripción:
Crea una agenda que permita agregar contactos (nombre, teléfono, correo) y los guarde en un archivo agenda.txt.
Al iniciar el programa, debe leer y mostrar los contactos existentes.
Funciones mínimas:
Ver contactos
Agregar contacto
Buscar contacto por nombre
Guardar automáticamente los cambios
Objetivo de aprendizaje:
Manejo de archivos (open, read, write)
Estructura modular (funciones)
Persistencia de datos
"""
import os 
AGENDA_FILE = "agenda.txt"

def cargar_contactos():
    contactos = []
    if os.path.exists(AGENDA_FILE):
        with open(AGENDA_FILE, "r") as archivo:
            for linea in archivo:
                nombre, telefono, correo = linea.strip().split(",")
                contactos.append({"nombre":nombre, "telefono":telefono, "correo":correo})
    return contactos

def guardar_contactos(contactos):
    with open(AGENDA_FILE, "w") as archivo:
        for contacto in contactos:
            archivo.write(f"{contacto['nombre']},{contacto['telefono']},{contacto['correo']}\n")
            
def ver_contactos(contactos):
    if not contactos:
        print("No hay contactos en la agenda.")
        return
    print("Contactos en la agenda:")
    for contacto in contactos:
        print(f"Nombre: {contacto['nombre']}, Teléfono: {contacto['telefono']}, Correo: {contacto['correo']}")
        
def agregar_contacto(contactos):
    nombre = input("Ingrese el nombre del contacto: ")
    telefono = input("Ingrese el teléfono del contacto: ")
    correo = input("Ingrese el correo del contacto: ")
    contactos.append({"nombre":nombre, "telefono":telefono, "correo":correo})
    guardar_contactos(contactos)
    print("Contacto agregado exitosamente.")
    
def buscar_contacto(contactos):
    nombre_buscar = input("Ingrese el nombre del contacto a buscar: ")
    encontrados = [c for c in contactos if c['nombre'].lower() == nombre_buscar.lower()]
    if encontrados:
        for contacto in encontrados:
            print(f"Contacto encontrado: Nombre: {contacto['nombre']}, Teléfono: {contacto['telefono']}, Correo: {contacto['correo']}")
    else:
        print("No se encontró ningún contacto con ese nombre.")
        
def main():
    contactos = cargar_contactos()
    while True:
        print("\n--- Mini Agenda ---")
        print("1. Ver contactos")
        print("2. Agregar contacto")
        print("3. Buscar contacto por nombre")
        print("4. Salir")
        opcion = input("Seleccione una opción (1-4): ")
        if opcion == '1':
            ver_contactos(contactos)
        elif opcion == '2':
            agregar_contacto(contactos)
        elif opcion == '3':
            buscar_contacto(contactos)
        elif opcion == '4':
            print("Saliendo de la agenda. ¡Hasta luego!")
            break
        else:
            print("Opción inválida. Por favor, intente de nuevo.")
            
if __name__ == "__main__":
    main()
        