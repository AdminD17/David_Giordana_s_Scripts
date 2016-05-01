# -*- coding: utf-8 -*-
import os
import sys

#Comprueba si el archivo es basura
def deleteFile(path):
    if path.endswith(".DS_Store"):
        print("Eliminando ".format(path))
        os.remove(path)
    if path.endswith("Thumbs.db"):
        print("Eliminando ".format(path))
        os.remove(path)

#Dada una ruta elimina los archivos basura
def removeDrunkFiles(path):
    #En el caso de ser un archivo
    if os.path.isfile(path):
        deleteFile(path)
        return
    #En el caso de ser un directorio
    elif os.path.isdir(path):
        fileList = os.listdir(path)
        for item in fileList:
            removeDrunkFiles(os.path.join(path, item))

#Main del script
def main():
    folderList = sys.argv[1:]
    for item in folderList:
        removeDrunkFiles(item)

#Lanza el programa
if __name__ == "__main__":
    main()
