def turnos_perfumeria():
    for t in range(1,1000):
        yield f"P- {t}"

def turnos_farmacia():
    for t in range(1,1000):
        yield f"F- {t}"

def turnos_cosmeticos():
    for t in range(1,1000):
        yield f"C- {t}"


turnos_p=turnos_perfumeria()
turnos_f=turnos_farmacia()
turnos_c=turnos_cosmeticos()


def decorador(opcion):

    print("\n" + "*" * 23)
    print("Su número es:")
    if opcion == "P":
        print(next(turnos_p))
    elif opcion == "F":
        print(next(turnos_f))
    else:
        print(next(turnos_c))
    print("Aguarde y será atendido")
    print("*" * 23 + "\n")