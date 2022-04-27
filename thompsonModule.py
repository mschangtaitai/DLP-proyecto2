
from math import fabs
from re import A
from module import *
op = ["(", "*", "+", "|", "©", ")", "?"]

def getSigma(er, mainAFN):
    for i in er:
        if (op.__contains__(i) == False):
            if(mainAFN.sigma.__contains__(i) == False):
                mainAFN.sigma.append(i)
    return mainAFN

def createLeafs(er, afnList):
    num = 0
    for i in er:
        if (op.__contains__(i) == False):
            initialS = "i" + i + "_" + str(num)
            finalS = "f" + i + "_" + str(num)
            afnList.append(AF([initialS, finalS], [i], [[initialS,i,finalS]], [initialS], [finalS]))
            num += 1

def replaceConcat(er):
    newEr = er
    prev = ""
    cont = 0
    for i in er:
        if ((i == ")") or (i == "|") or (prev == "|") or (prev == "(") or (prev == "") or (i == "*") or (i == "+") or (i == "?")) == False:
            newEr = newEr[:cont] + "©" + newEr[cont:]
            cont += 1
        cont += 1
        prev = i
    
    return newEr

def replaceOps(er):
    expresion = er

    expresion = expresion.replace("[","(")
    expresion = expresion.replace("{","(")
    expresion = expresion.replace("]",")?")
    expresion = expresion.replace("}",")*")
    expresion = expresion.replace("\n"," ╝") #Reemplazar ente
    expresion = expresion.replace("\t","╦") #Reemplazar tab
    expresion = expresion.replace("\r","║") #Reemplazar eol

    print(expresion)
    
    return expresion

def inToPos(infix):
    specials = {'?': 7, '+': 6, '*': 5, '©': 4, '|': 3}

    pofix = ""
    stack = ""

    # Loop through the string one character at a time
    for c in infix:
        if c == '(':
            stack = stack + c
        elif c == ')':
            while stack[-1] != '(':
                pofix, stack = pofix + stack[-1], stack[:-1]
            # Remove '(' from stack
            stack = stack[:-1]
        elif c in specials:
            while stack and specials.get(c, 0) <= specials.get(stack[-1], 0):
                pofix, stack = pofix + stack[-1], stack[:-1]
            stack = stack + c
        else:
            pofix = pofix + c

    while stack:
        pofix, stack = pofix + stack[-1], stack[:-1]
    
    return pofix


def concat(afn1,afn2):
    mutualState = afn1.finals[0] + afn2.start[0]
    states = list(set(afn1.states + afn2.states + [mutualState]) - set(afn1.finals) - set(afn2.start))
    sigma = afn1.sigma + [i for i in afn2.sigma if i not in afn1.sigma]
    trans = afn1.trans + afn2.trans
    for tran in trans:
        for i in tran:
            if((i == afn1.finals[0]) or (i == afn2.start[0])):
                tran[tran.index(i)] = mutualState
    
    return AF(states, sigma, trans, afn1.start, afn2.finals)

def opor(afn1,afn2):
    newStart = afn1.start[0] + afn2.start[0]
    newFinal = afn1.finals[0] + afn2.finals[0]
    states = afn1.states + afn2.states + [newStart] + [newFinal]
    sigma = afn1.sigma + [i for i in afn2.sigma if i not in afn1.sigma]
    trans = afn1.trans + afn2.trans
    trans.append([newStart,"ε",afn1.start[0]])
    trans.append([newStart,"ε",afn2.start[0]])
    trans.append([afn1.finals[0],"ε",newFinal])
    trans.append([afn2.finals[0],"ε",newFinal])

    return AF(states,sigma,trans,[newStart],[newFinal])

def kleene(afn):
    newStart = "new" + afn.start[0]
    newFinal = "new" + afn.finals[0]
    states = afn.states + [newStart] + [newFinal]
    trans = afn.trans

    trans.append([newStart,"ε",afn.start[0]])
    trans.append([afn.finals[0],"ε",newFinal])
    trans.append([afn.finals[0],"ε",afn.start[0]])
    trans.append([newStart,"ε",newFinal])

    return AF(states,afn.sigma,trans,[newStart],[newFinal])

def plus(afn):
    return concat(kleene(afn),afn)

def option(afn):
    trans = afn.trans

    trans.append([afn.start[0],"ε",afn.finals[0]])

    return AF(afn.states,afn.sigma,trans,afn.start,afn.finals)
