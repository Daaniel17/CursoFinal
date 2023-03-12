from random import randint

intentos = 0
estimado = 0
numero = randint(1,100)
nombre = input("Dime tu nombre: ")

print(f"Bueno {nombre}, adivina un número entre 1 y 100\nTienes 8 intentos para adivinar")

while intentos < 8:
    estimado = int(input("Cuál es el número?: "))
    intentos += 1

    if estimado < numero:
        print("El numero es mas alto")
    elif estimado > numero:
        print("El numero es mas bajo")
    else:
        print(f"Felicitaciones {nombre}! Has adivinado en {intentos} intentos")
        break

if estimado != numero:
    print(f"Lo siento, se han agotado los intentos. El numero secreto era {numero}")