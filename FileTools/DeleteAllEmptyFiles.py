# -*- coding: utf-8 -*-
import argparse
from os import walk, rmdir

#Dada una ruta elimina todas las carpetas vacías
def delEmptyDirs(src):
    for dirpath, _, _ in walk(src, topdown=False):  # Lista los archivos
        #Punto para detener el trabajo
        if dirpath == src:
            break
        #Intenta eliminar el directorio (falla si no está vacío)
        try:
            rmdir(dirpath)
        except OSError as ex:
            pass

def main():
    #Crea el parser
    parser = argparse.ArgumentParser()

    #Setea los argumentos
    parser.add_argument("--folder",
                        "-f",
                        type=str,
                        help="Ruta de la carpeta a eliminar"
                        )
    #Parsea la entrada y ejecuta el script
    args = parser.parse_args()
    delEmptyDirs(args.folder)

if __name__ == "__main__":
    main()
