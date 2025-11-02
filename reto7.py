# Simulador de cajero automatico
"""Descripcion: Simula un cajero con las siguientes funciones:
- Consultar saldo
- Retirar dinero
- Depositar dinero
- Salir
Objetivo del reto: Practicar el uso de funciones, condicionales y bucles en Python.
"""
def mostrar_menu():
    print("Bienvenido al Cajero Automático")
    print("1. Consultar saldo")
    print("2. Retirar dinero")
    print("3. Depositar dinero")
    print("4. Salir")

def consultar_saldo(saldo):
    print(f"Su saldo actual es: ${saldo:.2f}")
    
def retirar_dinero(saldo):
    monto = float(input("Ingrese el monto a retirar: $"))
    if monto > saldo:
        print("Fondos insuficientes.")
    else:
        saldo -= monto
        print(f"Ha retirado: ${monto:.2f}")
    return saldo

def depositar_dinero(saldo):
    monto = float(input("Ingrese el monto a depositar: $"))
    saldo += monto
    print(f"Ha depositado: ${monto:.2f}")
    return saldo

def main():
    saldo = 1000.00 # Saldo inicial
    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción (1-4): ")
        if opcion == '1':
            consultar_saldo(saldo)
        elif opcion == '2':
            saldo = retirar_dinero(saldo)
        elif opcion == '3':
            saldo = depositar_dinero(saldo)
        elif opcion == '4':
            print("Gracias por usar el Cajero Automático. ¡Hasta luego!")
            break
        else:
            print("Opción inválida. Por favor, intente de nuevo.")
            
if __name__ == "__main__":
    main()
    