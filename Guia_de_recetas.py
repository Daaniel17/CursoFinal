import os
from pathlib import Path
from os import system

ruta_archivo=Path("/home/juan/Documentos/CursoFinal/Recetas")

def contar(ruta):
    contador=0
    for i in Path(ruta).glob("**/*.txt"):
        contador+=1
    return contador

def inicio():
    system("clear")
    print("*"*27)
    print("* BIENVENIDO AL RECETARIO *")
    print("*"*27)
    print()
    print(f"La ruta de las recetas es : {ruta_archivo}")
    print(f"La cantidad de recetas son: {contar(ruta_archivo)}")    
 

    eleccion="x"

    while not eleccion.isnumeric() or int(eleccion) not in range(1,7):

        print("\n****Menu****")
        
        
        print()
        print("1.Leer receta")
        print("2.Crear receta")
        print("3.Crear categoria")
        print("4.Eliminar receta")
        print("5.Eliminar categoria")
        print("6.Salir del programa")
        print()


        eleccion=input("Elige una opcion: ")
    return int(eleccion)

def mostrar_categoria(ruta):
    print("CATEGORIAS:")
    lista_categorias=[]
    ruta_categoria=Path(ruta)
    contador=1

    for carpeta in ruta_categoria.iterdir():
        carpeta_string=str(carpeta.name)
        print(f"{contador}. {carpeta_string}")
        lista_categorias.append(carpeta)
        contador+=1
    return lista_categorias

def elegir_categoria(lista):
    eleccion_correcta="x"
    while not eleccion_correcta.isnumeric() or int(eleccion_correcta) not in range(1,len(lista)+1):
        eleccion_correcta=input("Elije una categoria:   ")
    return lista[int(eleccion_correcta)-1]

def mostrar_recetas(ruta):
    print("Recetas:")
    ruta_recetas = Path(ruta)
    lista_recetas = []
    contador = 1

    for receta in ruta_recetas.glob('*.txt'):
        receta_str = str(receta.name)
        print(f"[{contador}] - {receta_str}")
        lista_recetas.append(receta)
        contador += 1

    return lista_recetas


def elegir_recetas(lista):
    eleccion_receta = 'x'

    while not eleccion_receta.isnumeric() or int(eleccion_receta) not in range(1, len(lista) + 1):
        eleccion_receta = input("\nElije una receta: ")

    return lista[int(eleccion_receta) - 1]


def leer_receta(receta):
    print(Path.read_text(receta))


def crear_receta(ruta):
    existe = False

    while not existe:
        
        nombre_receta = input("Escribe el nombre de tu receta: ") + '.txt'
        
        contenido_receta = input("Escribe tu nueva receta: ")
        ruta_nueva = Path(ruta, nombre_receta)

        if not os.path.exists(ruta_nueva):
            Path.write_text(ruta_nueva, contenido_receta)
            print(f"Tu receta {nombre_receta} ha sido creada")
            existe = True
        else:
            print("Lo siento, esa receta ya existe")


def crear_categoria(ruta):
    existe = False

    while not existe:
        
        nombre_categoria = input("Escribe el nombre de la nueva categoria: ")
        ruta_nueva = Path(ruta, nombre_categoria)

        if not os.path.exists(ruta_nueva):
            Path.mkdir(ruta_nueva)
            print(f"Tu nueva categoria {nombre_categoria} ha sido creada")
            existe = True
        else:
            print("Lo siento, esa categoria ya existe")


def eliminar_receta(receta):
    Path(receta).unlink()
    print(f"La receta {receta.name} ha sido eliminada")


def eliminar_categoria(categoria):
    Path(categoria).rmdir()
    print(F"La categoria {categoria.name} ha sido eliminada")


def volver_inicio():
    eleccion_regresar = 'x'

    while eleccion_regresar.lower() != 'v':
        eleccion_regresar = input("\nPresione V para volver al menu: ")


finalizar_programa = False

while not finalizar_programa:
    menu = inicio()

    if menu == 1:
        mis_categorias = mostrar_categoria(ruta_archivo)
        mi_categoria = elegir_categoria(mis_categorias)
        mis_recetas = mostrar_recetas(mi_categoria)
        if len(mis_recetas) <1:
            print("No hay recetas en esta categoria.")
        else:
            mi_receta = elegir_recetas(mis_recetas)
            leer_receta(mi_receta)
        volver_inicio()
    elif menu == 2:
        mis_categorias = mostrar_categoria(ruta_archivo)
        mi_categoria = elegir_categoria(mis_categorias)
        crear_receta(mi_categoria)
        volver_inicio()
    elif menu == 3:
        crear_categoria(ruta_archivo)
        volver_inicio()
    elif menu == 4:
        mis_categorias = mostrar_categoria(ruta_archivo)
        mi_categoria = elegir_categoria(mis_categorias)
        mis_recetas = mostrar_recetas(mi_categoria)
        if len(mis_recetas) < 1:
            print("No hay recetas en esta categoria.")
        else:
            mi_receta = elegir_recetas(mis_recetas)
            eliminar_receta(mi_receta)
        volver_inicio()
    elif menu == 5:
        mis_categorias = mostrar_categoria(ruta_archivo)
        mi_categoria = elegir_categoria(mis_categorias)
        eliminar_categoria(mi_categoria)
        volver_inicio()
    elif menu == 6:
        finalizar_programa = True