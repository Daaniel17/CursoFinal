import numeros

def menu():
    print("Bienvenido a la farmacia.")
    print()

    while True:
        print("[P] Perfumeria, [F] Farmacia, [C] Cosmeticos")
        
        try:
            opcion=input("Elija la letra del area que desea: ").upper()
        except ValueError:
            print("Opcion no valida.")
        else:
            break

    numeros.decorador(opcion)


def inicio():

    while True:
        menu()
        try:
            otro_turno = input("Quieres sacar otro turno? [S] [N]: ").upper()
            ["S", "N"].index(otro_turno)
        except ValueError:
            print("Esa noes una opción válida")
        else:
            if otro_turno == "N":
                print("Gracias por su visita")
                break

inicio()


