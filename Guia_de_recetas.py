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
    
inicio()    



