# -*- coding: utf-8 -*-
import argparse
from os import remove
from os.path import splitext, isfile
from FileMethods import getPathFileList

acceptedExtensions = []
deniedExtensions = []

def deleteSelFiles(folder):
    fileList = getPathFileList([folder])
    for f in fileList:
        if not isfile(f):
            continue
        _, ext = splitext(f)

        if ext in acceptedExtensions: #Si el archivo debe ser aceptado
            continue
        elif ext in deniedExtensions: #Si el archivo debe ser rechazado
            remove(f)
        else: #Si aun no se ha registrado un comportamiento para la extensión
            while True:
                inData = input("¿Desea conservar la extensión \"{0}\"? S/n -> ".format(ext))
                if inData.lower().startswith("s"):
                    acceptedExtensions.append(ext)
                    break
                elif inData.lower().startswith("n"):
                    deniedExtensions.append(ext)
                    remove(f)
                    break

def main():
    parser = argparse.ArgumentParser()

    parser.add_argument("--folder",
                        "-f",
                        type=str,
                        help="Ruta de la carpeta a trabajar"
                        )
    args = parser.parse_args()

    deleteSelFiles(args.folder)


if __name__ == "__main__":
    main()
