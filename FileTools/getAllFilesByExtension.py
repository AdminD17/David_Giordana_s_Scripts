# -*- coding: utf-8 -*-
from FileMethods import getPathFileList
from os.path import isdir, isfile
from shutil import copy
import argparse

"""
Copia todos los archivos dentro de una lista de archivos que tengan una extension

Uso de la consola de comandos:
--files (-f) file_path_with_paths --dest (-d) dest_folder_path --extension (-d) Extension
"""

#Dada la ruta de un archivo retorna las las rutas de archivos en su interior
def readPathsFile(path):
    #Lee el contenido del archivo
    f = open(path, "r")
    lines = f.readlines()
    f.close()
    #Preserva y retorna las rutas válidas
    ret = []
    for item in lines:
        item = item.rstrip("\n")
        if isfile(item) or isdir(item):
            ret.append(item)
    return ret

#Dada una lista de archivos y una extensión, retorna los archivos que tienen esa extensión
def getAllFilesByExtension(fileList, extension):
    ret = []
    for item in fileList:
        if item.lower().endswith(extension.lower()):
            ret.append(item)
    return ret

#Dada una lista de aruchivos y la ruta de una carpeta copia todos los archivos en la carpeta
def copyFiles(fileList, destFolder):
    for item in fileList:
        copy(item, destFolder)
        print("Se copió el archivo: {0}".format(item))

#Copia todos los archivos dentro de una lista de archivos que tengan una extension
#
# pathsFile -> Ruta de un archivo con una lista de rutas
# destFolder -> Ruta de la carpteta de destino
# extension -> Extension que se quiere preservar
def extractAllFiles(pathsFile, destFolder, extension):
    paths = readPathsFile(pathsFile)
    paths = getPathFileList(paths)
    files = getAllFilesByExtension(paths, extension)
    copyFiles(files, destFolder)

#Metodo principal
def main():
    #Se crea el parser
    parser = argparse.ArgumentParser()

    #Argumento que toma
    parser.add_argument("--files",
                        "-f",
                        type=str,
                        help="Ruta del archivo que contiene la lista de archivos a procesar"
                        )

    #Argumento que toma
    parser.add_argument("--dest",
                        "-d",
                        type=str,
                        help="Ruta de la carpeta de destino"
                        )

    #Argumento que toma
    parser.add_argument("--extension",
                        "-e",
                        type=str,
                        help="Extension a aceptar"
                        )

    #Parsea los argumentos
    args = parser.parse_args()

    #Llama a la funcion que cumple la función del archivo
    extractAllFiles(args.files, args.dest, args.extension)

#Codigo llamado al ejecutar la aplicación
if __name__ == "__main__":
    main()
