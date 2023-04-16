import shutil
import os
import datetime
import time
import re
from pathlib import Path

shutil.unpack_archive("Proyecto+Dia+9.zip","Proyecto 9","zip")

ruta="/home/juan/Documentos/CursoFinal/Proyecto 9"

patron=r"N\D{3}\d{5}"

hoy= datetime.datetime.today()

def buscar_numero(archivo, patron):
    este_archivo = open(archivo, 'r')
    texto = este_archivo.read()
    if re.search(patron, texto):
        return re.search(patron, texto)
    else:
        return ''
