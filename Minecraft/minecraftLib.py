import math

#Dados dos puntos retorna los puntos opuestos ordenados de un cuadrante
def makeSquare((x1,y1), (x2,y2)):
    #Calcula los extremos
    minx = min(x1, x2)
    miny = min(y1, y2)
    maxx = max(x1, x2)
    maxy = max(y1, y2)
    return ((minx,miny), (maxx, maxy))

# Dado dos puntos opuestos de un cuadrante y el tamaño de un cuadrante
# retorna una lista de coordenadas de cuadrantes para relleno
def squarizator((x1,y1), (x2,y2), squareL):
    retList = []
    cantCol = int(math.ceil((x2 - x1) / float(squareL)))
    cantRow = int(math.ceil((y2 - y1) / float(squareL)))
    for x in range(cantCol):
        for y in range(cantRow):
            c1 = (x * squareL + x1, y * squareL + y1)
            c2 = ((x + 1) * squareL + x1, (y + 1) * squareL + y1)
            temp = (c1, c2)
            retList.append(temp)
    return _validator(x1, y1, x2, y2, retList)

# Dados los limites de un cuadrante y una lista de cuadrantes
# Valida las posiciones en caso de estar fuera de rango los valores
def _validator(x1l, y1l, x2l, y2l, lst):
    tempList = []
    for ((x1, y1), (x2, y2)) in lst:
        if x2 > x2l:
            x2 = x2l
        if y2 > y2l:
            y2 = y2l
        tempList.append(((x1, y1), (x2, y2)))
    return tempList
