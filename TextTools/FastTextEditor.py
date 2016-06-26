# -*- coding: utf-8 -*-
import os.path
import argparse

#Marcador de archivo editado
EDITED_MARK = "_WRT"

#Token de palabras a ignorar capitalizacion
IGNORED_TOKEN = "#I#"

#Token de palabras a capitalizar
CAPITALIZE_TOKEN = "#C#"

#Palabras de un archivo
words = []

#Palabras que se ignora la capitalizacion
ignoreCaseWords = []

#Nombres propios
capitalizeWords = []

#Dada una ruta lee el contenido de un archivo y retonra una lista de lineas
def readFile(path):
    #Extrae el contenido del archivo
    f = open(path, "r")
    content = f.readlines()
    f.close()
    #Lista de retorno con las lineas leidas
    retList = []
    #Codifica en unicode las lineas
    for item in content:
        value = item
        retList.append(value)
    return retList

#Dada la ruta del archivo original y el contenido, crea un archivo nuevo con el contenido
def writeFile(path, content):
    #Genera el nuevo nombre de archivo
    parentDirectory = os.path.dirname(path)
    temp = os.path.split(os.path.basename(path))[1]
    extension = (os.path.splitext(path))[1]
    fileName = os.path.splitext(temp)[0] + EDITED_MARK + extension
    newFileName = os.path.join(parentDirectory, fileName)
    #Escribe el archivo
    f = open(newFileName, "w")
    f.write(content)
    f.close()

#Compara dos strings
def compareStr(str1, str2):
    return str1.lower() == str2.lower()

#Dada una palabra y una lista de palabra revisa que esta se encuente en la lista ignorano la capitalizacion
def isIn(word, wordsList):
    for w in wordsList:
        if compareStr(w, word):
            return True
    return False

#Toma una palabra y la capitaliza en base a un booleano (Solo afecta a la primera letra)
def capitalize(word, capitalizeFirst=False):
    #En caso de tener que comenzar con mayuscula
    if capitalizeFirst:
        return word[0].upper() + word[1:].lower()
    #En caso de tener que comenzar con minúscula
    else:
        return word.lower()

#Toma una linea y la divide en una lista de palabras
def splitLine(line):
    #Elimina caracteres basura de la linea
    line = line.lstrip("\n")
    line = line.strip()
    if len(line) == 0:
        return []
    #Variable de retorno
    ret = []
    #Variable temporal para almacenar ultimo caacter procesado
    lastChar = line[0]
    #Palabra temporal para utilizar en procesamiento
    tempWord = ""

    #Procesa la linea
    for c in line:
        if c.isalpha():
            if lastChar.isalpha():
                tempWord += c
            elif tempWord != "":
                ret.append(tempWord)
                tempWord = "" + c

        elif c.isdigit():
            if lastChar.isdigit():
                tempWord += c
            elif tempWord != "":
                ret.append(tempWord)
                tempWord = "" + c

        else:
            if lastChar == c:
                tempWord += c
            elif tempWord != "":
                ret.append(tempWord)
                tempWord = "" + c

        lastChar = c

    #Agrega la ultima palabra para no evitar incluirla
    if tempWord != "":
        ret.append(tempWord)

    return ret

#Retorna un diccionario con las palabras asociadas a sus cantidades
def wordCounter():
    #diccionario con las cantidades
    ret = {}
    #Procesa la lista
    for w in words:
        #quita formato en caso de ser necesario
        temp = w.lower()
        if isIn(w, ignoreCaseWords) or isIn(w, capitalizeWords):
            temp = w
        #En caso de que la palabra ya esté registrada
        if temp in ret:
            ret[temp] += 1
        #Si la palabra no está registrada
        else:
            ret[temp] = 1
    return ret

#Convierte un diccionario en una lista de tuplas
def dictToList(dictionary):
    #Lista de retorno
    ret = []
    #Recorre el diccionario
    for k in dictionary:
        tup = (k, dictionary[k])
        ret.append(tup)
    return ret

#Dada una lista de (palabra, ocurrencias) y una cantidad
#Imprime las primeras "cantidad" palabras con sus ocurrencias
def printCountedWods(wordList, cant):
    getKey = lambda item: item[1]
    #Ordena la listas en base a las ocurrencias, con las mayores cantidades primero
    wordList = sorted(wordList, key=getKey , reverse=True)
    #Imprime el encabezado
    print("*"*50)
    print("Ocurrencias\t Palabras:\n")
    #Imprime las palabras
    cant = min(cant, len(wordList))
    if cant < 0:
        cant = len(wordList)
    for i in range(cant):
        print("{0}\t\t{1}".format(wordList[i][1], wordList[i][0]))
    print("*"*50)

#Toma una linea spliteada y la procesa para retornar un String
def processLine(originalLine):
    #Contiene la linea procesada
    line = ""
    #Variables de control internas
    ignoreNextSpace = False
    capitalizeNext = True

    #Procesa la linea
    for word in originalLine:
        #Si es una palabra
        if word.isalpha():
            #Si es una palabra ignorable
            if isIn(word, ignoreCaseWords):
                words.append(word)
                line += word
            #Si es necesario capitalizar
            elif isIn(word, capitalizeWords):
                tempWord = capitalize(word, True)
                line += tempWord
                words.append(tempWord)
            #Palabra común
            else:
                tempWord = capitalize(word, capitalizeNext)
                line += tempWord
                words.append(tempWord)
            capitalizeNext = False
            ignoreNextSpace = False
        #Si es un espacio
        elif word.isspace():
            if not ignoreNextSpace:
                line += " "
            ignoreNextSpace = False
        #Si son puntos suspensivos
        elif word.startswith("..."):
            line += "... "
            ignoreNextSpace = True
        #Si comienza con guion de dialogo
        elif word.startswith("--"):
            if line != "":
                line += " "
            line += "--"
            ignoreNextSpace = True
            capitalizeNext = True



    #Agrega punto final
    line = line.strip()
    if not line.endswith("."):
        line += "."

    #Retorna la linea procesada
    return line

#Dada la ruta de un archivo parsea un diccionario de reglas
def parseDictionary(path):
    if path == "":
        return
    content = readFile(path)
    for line in content:
        line = line.rstrip("\n")
        # Caso palabra a ignorar capitalizacion
        if line.startswith(IGNORED_TOKEN):
            temp = line[4:].strip()
            ignoreCaseWords.append(temp)
        # Caso palabra capitalizada
        elif line.startswith(CAPITALIZE_TOKEN):
            temp = line[4:].strip()
            capitalizeWords.append(temp)

#Funcion que dado un archivo de texto crea uno nuevo editado
def writeText(filePath, dictPath, cantShow):
    #Parsea el diccionario
    parseDictionary(dictPath)
    #Lineas del archivo original
    originalContent = readFile(filePath)
    #Contenido del nuevo archivo
    newContent = ""

    for item in originalContent:
        words = splitLine(item)
        line = processLine(words)
        newContent += line + "\n"

    #Lista de tuplas (palabra, ocurrencias)
    wordCant = dictToList(wordCounter())
    #Imprime la lista
    printCountedWods(wordCant, cantShow)

    #Escribe el nuevo archivo
    writeFile(filePath, newContent)

#Metodo que se lanza al iniciar el programa
def main():
    #Crea el parser
    parser = argparse.ArgumentParser()

    #Argumento que toma la ruta del archivo de texto
    parser.add_argument("--file",
                        "-f",
                        type=str,
                        help="Ruta del archivo de texto a procesar")

    #Argumento que toma la cantidad de palabras a mostrar
    parser.add_argument("--wordcounter",
                    "-w",
                    type=int,
                    help="Cantidad de palabras a mostrar por el contador. Newgativo para imprimir todo",
                    default=0)

    #Argimento que toma la ruta del archivo del diccionario
    parser.add_argument('-d',
                        '--dictionary',
                        type=str,
                        help='Ruta del diccionario, para aplicar reglas y excepciones',
                        default='')

    #Parsea los argumentos y llama a las funciones correspondientes
    args = parser.parse_args()
    writeText(args.file, args.dictionary, args.wordcounter)

if __name__ == "__main__":
    main()
