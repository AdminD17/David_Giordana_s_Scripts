import sys
from fillMinecraft import *;

"""
ORDEN DE LOS ARGUMENTOS

X1 Z1 X2 Z2 Y Bloques_de_alto Material 

"""

def main():
    if len(sys.argv) < 7:
        print "Error: no hay suficientes argumentos"
        return
    x1 = int(sys.argv[1])
    y1 = int(sys.argv[2])
    x2 = int(sys.argv[3])
    y2 = int(sys.argv[4])
    level = int(sys.argv[5])
    cant = int(sys.argv[6])
    if len(sys.argv) >= 8:
        fillMinecraft((x1,level,y1) , (x2,level + (cant - 1),y2), sys.argv[7])
    else:
        fillMinecraft((x1,level,y1) , (x2,level + (cant - 1),y2))
    return

if __name__ == "__main__":
    main()
