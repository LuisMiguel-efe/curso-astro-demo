# Calculadora de propinas

def calcular_propina(cuenta, porcentaje_propina):
    """Calcula la propina basada en el total de la cuenta y el porcentaje de propina.

    Args:
        cuenta (float): El total de la cuenta.
        porcentaje_propina (float): El porcentaje de propina a calcular (por ejemplo, 0.15 para 15%).

    Returns:
        float: La cantidad de propina.
    """
    return cuenta * porcentaje_propina
def main():
    try:
        cuenta = float(input("Ingrese el total de la cuenta: "))
        porcentaje_propina = float(input("Ingrese el porcentaje de propina (por ejemplo, 0.15 para 15%): "))
        
        propina = calcular_propina(cuenta, porcentaje_propina)
        print(f"La propina calculada es: ${propina:.2f}")
        print(f"El total a pagar es : ${cuenta + propina:.2f}")
    except ValueError:
        print("Por favor, ingrese valores numéricos válidos.")
        
if __name__ == "__main__":
    main()