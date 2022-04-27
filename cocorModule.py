from module import *

def combineAF(afnList):
    stateCount = 1
    tokenCount = 0
    newStates = ["0"]
    newSigma = []
    newTrans = []
    newStart = ["0"]
    newFinals = []
    tokens = []

    for i in afnList:

        newSigma = newSigma + list(set(i.sigma) - set(newSigma))
        # newSigma = newSigma + i.sigma
        for state in i.states:
            newStates.append(str(stateCount))
            if (state in i.start):
                newTrans.append(["0","ε",str(stateCount)])
            if (state in i.finals):
                newFinals.append(str(stateCount))
                tokens.append([str(tokenCount),str(stateCount)])
            for tran in i.trans:
                newTran = tran
                if tran[0] == state:
                    newTran[0] = str(stateCount)
                if tran[2] == state:
                    newTran[2] = str(stateCount)
                newTrans.append(tran)
            stateCount += 1
        tokenCount += 1


    return([AF(newStates,newSigma,newTrans,newStart,newFinals),tokens])