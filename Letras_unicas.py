"""Escribe una función (puedes ponerle cualquier nombre que quieras) que 
reciba cualquier palabra como parámetro, y que
devuelva todas sus letras únicas (sin repetir) pero en orden alfabético.
Por ejemplo si al invocar esta función pasamos la palabra
"entretenido", debería devolver ['d', 'e', 'i', 'n', 'o', 'r', 't']"""

def unica(palabra):
    mi_set=set()

    for letra in palabra:
        mi_set.add(letra)

        lista=list(mi_set)
        lista.sort()

        return lista