# -*- coding: utf-8 -*-
import os
import ntpath
from os import listdir
from os.path import isdir, isdir, join

#Lista de archivos a ignorar
IGNORED_FILES = {
                ".DS_Store",
                ".DocumentRevisions-V100"
                }

#Indica si un archivo es ignorable, Generalmente generados por el sistema
def isIgnorableFile(path):
    name = ntpath.basename(path)
    for i in IGNORED_FILES:
        if i in name:
            return True
    return False

#Dada la ruta de un directorio, retorna la ruta de todo su contenido
def folderToPathList(parentFolder):
    #Evita ejecutar en caso innecesario
    if not isdir(parentFolder):
        return [].append(parentFolder)

    #Lista del conteniido
    tempList = listdir(parentFolder)
    #Lista de retorno
    retList = []
    for item in tempList:
        path = join(parentFolder, item)
        retList.append(path)
    return retList

#Dada una lista de rutas retorna una lista con la ruta de todos los archivos internos
def getPathFileList(lst=[]):
    ret = []
    for item in lst:
        #Caso archivo ignorable
        if isIgnorableFile(item):
            continue
        #En caso de ser un archivo
        elif isfile(item):
            ret.append(item)
        #En caso de ser un directorio
        elif isdir(item):
            folderItems = folderToPathList(item)
            ret.extend(getPathFileList(folderItems))
    return ret

if __name__ == "__main__":
    l = []
    l.append("/Users/Gally/Desktop/Sayonara Zetsubō Sensei")
    a = getPathFileList(l)
    for s in a:
        print(s)
