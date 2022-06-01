from thompson import *
from subconjuntos import *
from minizacion import *
import time
from afdSimulator import *
from afnSimulator import *
from cocorModule import *
from thompsonModule import *


def readFile(fileName):
    file = open(fileName, "r", encoding="utf-8")
    lines = file.readlines()

    chars = []
    keys = []
    tokens = []
    productions = []

    modo = ""
    prod = ""
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
        
        elif (line.split(" ")[0] == "PRODUCTIONS"):
            modo = "productions"

        else:    
            if(modo == "tokens"):
                try:
                    tokens.append([line.split(" ")[0],line.split(" ")[2].replace(".","")])
                except:
                    print("No token")

            elif(modo == "characters"):
                try:
                    chars.append([line.split(" ")[0],(line.split(" ",2)[2]).replace('"',"").replace("+","").replace("'","").replace("..","~").replace(".","")])
                except:
                    print("No chars")
            
            elif(modo == "keywords"):
                try:
                    keys.append([line.split(" ")[0],line.split(" ",2)[2].replace(".","").replace('"',"")])
                except:
                    print("No keys")
            elif(modo == "productions"):
                try:
                    lineClean = ""
                    prev = ""
                    add = True
                    for i in line:
                        if ((add == True) and (i != "<")):
                            lineClean = lineClean + i
                            if(lineClean[-2:] == "(."):
                                lineClean = lineClean[:len(lineClean)-2]
                        if (i == "<"):
                            add = False
                        elif (i == ">"):
                            add = True
                        elif ((i == ".") and (prev == "(")):
                            add = False
                        elif ((i == ")") and (prev == ".")):
                            add = True
                        
                        prev = i
                    
                    if(line.startswith(("\t"))):
                        prod = prod + lineClean
                    elif(len(line) == 0):
                        print("no line")
                    else:
                        productions.append(prod)
                        prod = lineClean
                        
                except:
                    print("No prod")

    productionsClean = []
    # print("Productions: ")
    for i in productions:
        # print(i)
        cleaned = i.replace("\t","").replace(" ","")[:-1].split("=")
        if (len(cleaned) == 2):
            productionsClean.append(cleaned)
   
    print("Productions Clean: ")    
    for i in productionsClean:
        print(i)

    

    print("Chars: ")
    for i in chars:
        print(i)

    for i in chars:
        if ("CHR(" in i[1]):
            placeCHR = (i[1].index("CHR("))
            placeCHRF = (i[1].index(")"))
            part1 = (i[1][:placeCHR])
            part3 = (i[1][placeCHRF + 1:])
            intchr = int((i[1][placeCHR:placeCHRF + 1]).replace("CHR(","").replace(")",""))

            charReplace = chr(intchr)
            i[1] = part1 + charReplace + part3

        if ("~" in i[1]):
            newStr = ''
            startChar = ord(i[1][0])
            endChar = ord(i[1][2]) + 1

            for char in range(startChar,endChar):
                newStr = newStr + str(chr(char))
            
            print('newStr')
            print(newStr)
            
            i[1] = str(newStr)


    
    charList = []
    charListSorted = []
    for i in chars:
    
        for j in charListSorted:
            if (j in i[1]):
                print(j,i[1])
                i[1] = i[1].replace(j,chars[charList.index(j)][1]).replace("+","")
        charList.append(i[0])
        charListSorted = sorted(charList, key=len, reverse=True)

    for char in chars:
        newStr = ''
        for i in char[1]:
            if i not in newStr:
                newStr += i

        char[1] = newStr

    for i in chars:
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
        # afdList.append(afn)

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
