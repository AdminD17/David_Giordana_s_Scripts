import sys
from minecraftLib import *;

"""
ODEN DE LOS ARGUMENTOS
X1 Y1 Z1 X2 Y2 Z2 material
-Los pirmeros seis argumentos son para establecer las coordenadas del espacio
a rellenar
-Material: nombre del material para rellenar (Default = Air)
"""

#Maxima cantidad de bloques
MAX_BLOCK = 32768

#Nivel del piso y techo
minY = 0
maxY = 0

#Medida del lado de cuadrante
squareL = 0

#DAda unas coordenadas las parsea para el procesamiento
def parseCoordinates((x1,y1,z1) , (x2,y2,z2)):
    global squareL
    global minY
    global maxY
    minY = min(y1, y2)
    maxY = max(y1, y2)
    squareL = int(math.floor(math.sqrt(MAX_BLOCK / max((y2 - y1), 1))))
    squareL -= 10
    return

#Dada una lista de comandos y un material imprime la salida
def printCommand(lst, material):
    for ((x1,y1), (x2,y2)) in lst:
        print "/fill {0} {1} {2} {3} {4} {5} {6}".format(x1, minY, y1, x2, maxY, y2, "minecraft:" + material)

#Calcula el campo a rellenar
def fillMinecraft((x1,y1,z1), (x2,y2,z2), material="air"):
    parseCoordinates((x1,y1,z1) , (x2,y2,z2))
    sq = makeSquare((x1,z1), (x2,z2))
    coordinatesList = squarizator(sq[0] , sq[1], squareL)
    printCommand(coordinatesList, material)

#Lanza el programa
def main():
    if len(sys.argv) < 7:
        print "Error: no hay suficientes argumentos"
        return
    x1 = int(sys.argv[1])
    y1 = int(sys.argv[2])
    z1 = int(sys.argv[3])
    x2 = int(sys.argv[4])
    y2 = int(sys.argv[5])
    z2 = int(sys.argv[6])
    if len(sys.argv) >= 8:
        fillMinecraft((x1,y1,z1) , (x2,y2,z2), sys.argv[7])
    else:
        fillMinecraft((x1,y1,z1) , (x2,y2,z2))
    return

if __name__ == "__main__":
    main()
    #print "END"
