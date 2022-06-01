
from module import *

def afnSimulator(afn, w):
    s = eClosure(afn.start,afn.trans)
    for i in w:
        currentW += i
        s = eClosure(move(s,i,afn.trans),afn.trans)

    for i in s:
        if i in afn.finals:
            return [True,i]
    return [False,None]

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
