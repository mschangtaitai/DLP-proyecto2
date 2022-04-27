from thompson import *
from subconjuntos import *
from minizacion import *
import time
from afdSimulator import *
from afnSimulator import *
from cocorModule import *

# file = open("cocor.txt", "r")
# file = open("Double.ATG", "r")
file = open("Aritmetica.ATG", "r")

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
                keys.append([line.split(" ")[0],line.split(" ",2)[2]])
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
        print(intchr)
        print(chr(9))
        charReplace = chr(intchr)
        print(charReplace)
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

for i in range(len(tokens)):
    start_time = time.time()
    afn = thompson(tokens[i][1])
    # graphAF(afn, "AFN")
    print("AFN terminado")
    final_time = time.time() - start_time
    print(final_time)
    print(afnSimulator(afn,"hola123b"))

    start_time = time.time()
    afd = subconjuntos(afn)
    # graphAF(afd, "AFD")
    print("AFD terminado")
    final_time = time.time() - start_time
    print(final_time)
    print(afdSimulator(afd,"123b"))

    start_time = time.time()
    afdmin = minAFD(afd)
    # graphAF(afdmin, "AFDmin")
    print("Min terminado")
    final_time = time.time() - start_time
    print(final_time)
    print(afdSimulator(afdmin,"123b"))
    afdList.append(afdmin)

print(len(afdList))

print(afdSimulator(afdList[0],"123b"))
print(afdSimulator(afdList[1],"168481313"))

combinedAF, tokenList = combineAF(afdList)
print(tokenList)

w1, t1 = (afnSimulator(combinedAF,"hola123b"))
print(w1)
print(t1)
if (w1 == True):
    print("Soy true")
    for i in tokenList:
        print(i)
        print(i[1],t1)
        print(i[1] == t1)
        if (i[1] == t1):
            print("Si")
            print(tokens[int(i[0])][0])

w2, t2 = (afnSimulator(combinedAF,"168481313h"))

print(w2)
print(t2)


