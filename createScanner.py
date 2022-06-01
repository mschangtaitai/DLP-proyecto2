from module import *
from readFile import *

combinedAF, tokenList, tokens, keys = readFile("2.atg")

AFStates = "['" + "', '".join(combinedAF.states) + "']"
AFSigma = "['" + "', '".join(combinedAF.sigma) + "']"

AFTrans = "["
for i in combinedAF.trans:
    AFTrans += "['" + "', '".join(i) + "'],"
AFTrans = AFTrans[:-1] + "]"

AFStart = "['" + "', '".join(combinedAF.start) + "']"
AFFinals = "['" + "', '".join(combinedAF.finals) + "']"

AFString = "combinedAF = AF(" + AFStates + "," + AFSigma + "," + AFTrans + "," + AFStart + "," + AFFinals + ")\n"
print(AFString)


tokenListString = "tokenList = ["
for i in tokenList:
    tokenListString += "['" + "', '".join(i) + "'],"
tokenListString = tokenListString[:-1] + "]\n"

tokensString = "tokens = ["
for i in tokens:
    tokensString += "['" + "', '".join(i) + "'],"
tokensString = tokensString[:-1] + "]\n"

keysString = "keys = ["
for i in keys:
    print(i)
    keysString += "['" + "', '".join(i) + "'],"
if len(keys) > 0:
    keysString = keysString[:-1] + "]\n"
else:
    keysString = keysString + "]\n"



output = open("scanner.py", "w+", encoding="utf-8")
output.write("""
from module import *
from afnSimulator2 import *
""")
output.write(AFString)
output.write(tokenListString)
output.write(tokensString)
output.write(keysString)

output.write("""
keyValues = []
for key in keys:
    keyValues.append(key[1])

testFileName = input("Ingrese el nombre del archivo: ")
file = open(testFileName, "r")
lines = file.readlines()

x = ''
for line in lines:
    x = x + line        

print('x')
print(x)

response = (afnSimulator2(combinedAF, x, keyValues))
cont = 0
for item in response:
    for t in tokenList:
        if (item == t[1]):
            response[cont] = tokens[int(t[0])][0]
    
    cont += 1
print(response)
""")



