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
    return eleccion

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
        eleccion_correcta=input("Elije una categotia:   ")
    return lista[(eleccion_correcta)-1]