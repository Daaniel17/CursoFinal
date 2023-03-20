def ceros(*args):
    buscador=0

    for n in args:
        if args[buscador] == 0 and args[buscador + 1] == 0:
            return True
        else:
            buscador += 1
    return False
