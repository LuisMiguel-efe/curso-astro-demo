"""
🧩 Reto 4: Gestor de Tareas (Nivel 4 – Avanzado)
Descripción: Crea un mini programa de consola para gestionar tareas.
Debe permitir: Agregar tarea, Listar tareas, Marcar tarea como completada, Eliminar tarea.
Objetivo de aprendizaje:
Listas, diccionarios
Menús interactivos
Bucles y lógica de control
"""
def show_menu():
    print("\nGestor de Tareas")
    print("1. Agregar tarea ➕")
    print("2. Listar tareas 📝")
    print("3. Marcar tarea como completada ✅")
    print("4. Eliminar tarea 🗑️")
    print("5. Salir 🚪")
    
def agregar_tarea(tareas):
    tarea = input("Ingrese la descripción de la tarea: ")
    tareas.append({"descripcion": tarea, "completada": False})
    print("Tarea agregada. ✅")
    
def listar_tareas(tareas):
    if not tareas:
        print("No hay tareas pendientes. 🎉")
        return
    for idx, tarea in enumerate(tareas, start=1):
        estado = "✅" if tarea["completada"] else "❌"
        print(f"{idx}. {tarea['descripcion']} [{estado}]")
        
def marcar_completada(tareas):
    listar_tareas(tareas)
    try:
        indice = int(input("Ingrese el número de la tarea a marcar como completada: ")) - 1
        if 0 <= indice < len(tareas): 
            tareas[indice]["completada"] = True
            print("Tarea marcada como completada. ✅")
        else:
            print("Número de tarea inválido. ❌")
    except ValueError:
        print("Entrada inválida. Por favor, ingrese un número. ❌")
        
def eliminar_tarea(tareas):
    listar_tareas(tareas)
    try:
        indice = int(input("Ingrese el número de la tarea a eliminar: ")) - 1
        if 0 <= indice < len(tareas):
            tareas.pop(indice)
            print("Tarea eliminada. 🗑️")
        else:
            print("Número de tarea inválido. ❌")
    except ValueError:
        print("Entrada inválida. Por favor, ingrese un número. ❌")

def main():
    tareas = []
    while True:
        show_menu()
        opcion = input("Seleccione una opción (1-5): ")
        if opcion == '1':
            agregar_tarea(tareas)
        elif opcion == '2':
            listar_tareas(tareas)
        elif opcion == '3':
            marcar_completada(tareas)
        elif opcion == '4':
            eliminar_tarea(tareas)
        elif opcion == '5':
            print("Saliendo del gestor de tareas. ¡Hasta luego! 👋")
            break
        else:
            print("Opción inválida. Por favor, intente de nuevo. ❌")
            
if __name__ == "__main__":
    main()