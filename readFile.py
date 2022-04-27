from thompson import *
from subconjuntos import *
from minizacion import *
import time
from afdSimulator import *
from afnSimulator import *
from cocorModule import *
from thompsonModule import *

def readFile(fileName):
    file = open(fileName, "r")
    lines = file.readlines()

    chars = []
    keys = []
    tokens = []

    modo = ""
    for line in lines:
        line = line.replace("\n","")
        if (line.split(" ")[0] == "TOKENS"):
            modo = "tokens"
        
        elif (line.split(" ")[0] == "PRODUCTIONS"):
            modo = "productions"

        elif (line.split(" ")[0] == "CHARACTERS"):
            modo = "characters"
        
        elif (line.split(" ")[0] == "KEYWORDS"):
            modo = "keywords"
        

        else:    
            if(modo == "tokens"):
                try:
                    tokens.append([line.split(" ")[0],line.split(" ")[2].replace(".","")])
                except:
                    print("No token")

            elif(modo == "characters"):
                try:
                    chars.append([line.split(" ")[0],(line.split(" ",2)[2]).replace('"',"").replace("+","").replace("'","").replace(".","")])
                except:
                    print("No chars")
            
            elif(modo == "keywords"):
                try:
                    keys.append([line.split(" ")[0],line.split(" ",2)[2].replace(".","").replace('"',"")])
                except:
                    print("No keys")


    print("Chars: ")
    charList = []
    charListSorted = []
    for i in chars:

        for j in charListSorted:
            if (j in i[0]):
                i[1] = i[1].replace(j,chars[charList.index(j)][1]).replace("+","")
        charList.append(i[0])
        charListSorted = sorted(charList, key=len, reverse=True)

    for i in chars:
        print(i)
        if ("CHR(" in i[1]):
            placeCHR = (i[1].index("CHR("))
            placeCHRF = (i[1].index(")"))
            part1 = (i[1][:placeCHR])
            part3 = (i[1][placeCHRF + 1:])
            intchr = int((i[1][placeCHR:placeCHRF + 1]).replace("CHR(","").replace(")",""))

            charReplace = chr(intchr)
            i[1] = part1 + charReplace + part3
        else:
            i[1] = "|".join(i[1])

    print("Chars")
    for i in chars:
        print(i)


    print("Tokens: ")
    for i in tokens:
        for j in charListSorted:
            if (j in i[1]):
                i[1] = i[1].replace(j,"(" + chars[charList.index(j)][1] + ")").replace('"',"")
        print(i)

    print("Keys: ")
    for i in keys:
        print(i)

    afdList = []
    print("READ FILE")
    cont = 0
    for t in tokens:
        tokens[cont][1] = replaceOps(t[1])
        cont += 1
    print(tokens)
    

    for i in range(len(tokens)):
        start_time = time.time()
        afn = thompson(tokens[i][1])
        # graphAF(afn, "AFN")
        print("AFN terminado")
        final_time = time.time() - start_time
        print(final_time)

        start_time = time.time()
        afd = subconjuntos(afn)
        # graphAF(afd, "AFD")
        print("AFD terminado")
        final_time = time.time() - start_time
        print(final_time)

        start_time = time.time()
        afdmin = minAFD(afd)
        # graphAF(afdmin, "AFDmin")
        print("Min terminado")
        final_time = time.time() - start_time
        print(final_time)
        afdList.append(afdmin)
    
    


    return(combineAF(afdList) + [tokens] + [keys])
