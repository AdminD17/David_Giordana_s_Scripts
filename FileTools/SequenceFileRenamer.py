# -*- coding: utf-8 -*-
#Usada para leer argumentos de la consola
import argparse
#Usado para trabajar con los archivos
from os import rename
from os.path import dirname, splitext, join
from shutil import copy, rmtree
from FileMethods import folderToPathList

#Renombra un archivo
#
# path -> Ruta del archivo a renombrar
# number -> numero por el que se renombra el archivo
# digitNumber -> Cantidad de dígitos máximos de un nombre
def renameWithNumber(path, number, digitNumber):
    #Extrae los datos para la operación
    parentDirectory = dirname(path)
    fileNumber = str(number).zfill(digitNumber)
    extension = (splitext(path))[1]

    #Crea la nueva ruta
    newFileName = join(parentDirectory, fileNumber + extension)

    #Renombra el archivo
    rename(path, newFileName)

# Dada dos listas las combina en una
def combineLists(even, odd):
    isEven = False
    ret = []
    while even != [] or odd != []:
        if isEven:
            if even != []:
                ret.append(even.pop(0))
            else:
                ret.append(odd.pop(0))
        else:
            if odd != []:
                ret.append(odd.pop(0))
            else:
                even.append(even.pop(0))
        isEven = not isEven
    return ret

# Dada una carpeta de elementos impares y una de elementos pares las Combina
# y en una carpeta de destino renombrandolas en el proceso
def combineFolder(evenPath, oddPath, destFolder):
    #Lista los archivos necesarios
    evenList = folderToPathList(evenPath)
    oddList = folderToPathList(oddPath)

    #Combina las listas
    renameList = combineLists(evenList, oddList)

    #Renombra los archivos
    digits = len(str(len(renameList)))
    for i in range(len(renameList)):
        renameWithNumber(renameList[i], i+1, digits)

    #Recarga la lista de archivos
    evenList = folderToPathList(evenPath)
    oddList = folderToPathList(oddPath)

    #Copia los archivos a la carpeta de destino
    for item in evenList:
        copy(item, destFolder)
    for item in oddList:
        copy(item, destFolder)
    #Borra las carpetas
    rmtree(evenPath)
    rmtree(oddPath)

#Metodo lanzado al principio de la ejecución
def main():
    #Se crea el parser
    parser = argparse.ArgumentParser()

    #Argumento que toma la carpeta de contenido par
    parser.add_argument("--even",
                        "-e",
                        type=str,
                        help="Ruta de la carpeta con contenido par"
                        )

    #Argumento que toma la carpeta de contenido impar
    parser.add_argument("--odd",
                        "-o",
                        type=str,
                        help="Ruta de la carpeta con contenido impar"
                        )

    #Argumento que toma la carpeta de destino
    parser.add_argument("--destiny",
                        "-d",
                        type=str,
                        help="Ruta de la carpeta de destino"
                        )

    #Parsea los argumentos
    args = parser.parse_args()

    #Renombra los archivos
    combineFolder(args.even, args.odd, args.destiny)


if __name__ == "__main__":
    main()
