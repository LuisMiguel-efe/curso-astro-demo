import random


def game():
    secret_number = random.randint(1, 100)
    tries = 0
    guessed = False
    
    print("¡Bienvenido al juego de adivinar el número!")
    print("He seleccionado un número entre 1 y 100. ¿Puedes adivinar cuál es?")

    while not guessed:
        try:
            guess = int(input("Ingresa tu suposición: "))
            tries += 1
            if guess < secret_number:
                print("Demasiado bajo. Intenta de nuevo.")
            elif guess > secret_number:
                print("Demasiado alto. Intenta de nuevo.")
            else:
                guessed = True
                print(f"¡Felicidades! Has adivinado el número {secret_number} en {tries} intentos.")
        except ValueError:
            print("Por favor, ingresa un número válido.")
 
if __name__ == "__main__":
    game()               
    print("Quieres jugar de nuevo? (s/n)")
    replay = input().lower()
    if replay == 's':
        game()
    else:
        print("Gracias por jugar. ¡Hasta luego!")
        