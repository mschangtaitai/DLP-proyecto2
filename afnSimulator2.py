
from module import *

def afnSimulator2(afn, w, keys):
    currentW = ""
    s = eClosure(afn.start,afn.trans)
    response = []
    for i in w:
        currentW += i
        prevS = s
        s = eClosure(move(s,i,afn.trans),afn.trans)
        if(currentW in keys):

            response.append(currentW)
            currentW = ""
            s = eClosure(afn.start,afn.trans)

        if((len(s) == 0) and (i == " ")):
            for j in prevS:
                if j in afn.finals:
                    response.append(j)
                    break
            currentW = ""
            s = eClosure(afn.start,afn.trans)
    for j in prevS:
        if ((j in afn.finals) and (currentW != "")):
            response.append(j)
            break

    s = eClosure(afn.start,afn.trans)
        

    return response

#Area de pruebas

# (a|b)*abb
# testAFN = AF(["0","1","2","3","4","5","6","7","8","9","10"], ["a","b"], [
#     ["0","ε","1"],
#     ["0","ε","7"],
#     ["1","ε","2"],
#     ["1","ε","4"],
#     ["2","a","3"],
#     ["3","ε","6"],
#     ["4","b","5"],
#     ["5","ε","6"],
#     ["6","ε","1"],
#     ["6","ε","7"],
#     ["7","a","8"],
#     ["8","b","9"],
#     ["9","b","10"],
#     ], ["0"], ["10"])

# cadena = "abababb"

# result = afnSimulator(testAFN,cadena)
# print(result)
