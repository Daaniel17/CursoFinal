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



