import numpy as np
import string
import argparse

fileName = "task_2_input.txt"
expression_chars = ['(', ')', '+', '*', '?', '|', '.']
operators = ['+', '*', '?', '|', '.']
special_operators = ['+', '*', '?', '.']

# FIXME: test case 6
class stack:
    array = []

    def push(self, el):
        self.array.append(el)

    def top(self):
        if(len(self.array) == 0):
            return None
        return self.array[len(self.array)-1]

    def pop(self):
        if self.empty():
            return None
        popped = self.array[len(self.array)-1]
        self.array = self.array[:len(self.array)-1]
        return popped

    def empty(self):
        return len(self.array) == 0


class NFA:
    def __init__(self, initialState, finalState, states, transitions, alpha=[]):
        self.initialState = initialState
        self.finalState = finalState
        self.states = states
        self.alphapet = alpha
        self.transitions = transitions

    def addTransitions(self, newTrans):
        for tran in newTrans:
            self.transitions.append(tran)

    def getStatesLen(self):
        return len(self.states)

    def getStates(self):
        return self.states

    def getTransitions(self):
        return self.transitions

    def __str__(self):
        printStr = ""
        # printStr += "States:\n"
        printStr += ",".join("q"+(str(x)) for x in self.states)
        printStr += "\n"
        # printStr += "Alpha:\n"
        printStr += ",".join(str(x) for x in self.alphapet)
        printStr += "\n"
        printStr += ("q" + str(self.initialState) + "\n")
        printStr += ("q" + str(self.finalState) + "\n")
        # printStr += "transitions:\n"
        printStr += ", ".join(("(q" + str(x['from']) + ", " + x['tran'] + ", [" + ",".join(
            ("q" +str(s)) for s in x['to']) + "])") for x in self.transitions)
        # printStr += "\n"
        return printStr


def isAlpha(char):
    return not char in expression_chars


def sanitaizeExpression(exp):
    newExp = ""
    idx = -1
    for char in exp:
        idx += 1
        if idx > 0:
            prev = exp[idx-1]
            if (prev != '|' and prev != '(') and (isAlpha(char) or char == '('):
                # two consequent alphas, alpha and special operand before it, alpha and closing bracket before it
                newExp += "."
        newExp += char
    newExp = newExp.replace("e", " ")
    return newExp


def getPriorityofOp(operand):
    switcher = {
        '*': 4,
        '+': 4,
        '?': 4,
        '.': 3,
        '|': 2
    }
    # print(operand, switcher.get(operand, 0))
    return switcher.get(operand, 0)


def infixToPostfix(infixExp):
    postfix = ""
    operandsStack = stack()
    for char in infixExp:
        if(isAlpha(char)):
            postfix += char
        elif char == '(':
            operandsStack.push(char)
        elif char == ')':
            while(not operandsStack.top() == '('):
                postfix += operandsStack.pop()
            operandsStack.pop()
        else:
            while(not operandsStack.empty() and getPriorityofOp(operandsStack.top()) >= getPriorityofOp(char)):
                postfix += operandsStack.pop()
            operandsStack.push(char)
        # print(stack.array)
        # print(postfix)
    while(not operandsStack.empty()):
        postfix += operandsStack.pop()
    return postfix


def concat(firstNFA, secondNFA):
    print("first nfa")
    print(firstNFA)
    newStates = []
    maxLen = len(firstNFA.getStates()) - 1
    for state in firstNFA.getStates():
        newStates.append(state)
    for state in secondNFA.getStates()[1:]:
        newStates.append(state+maxLen)

    newTransitions = firstNFA.getTransitions()
    print(newTransitions)
    for trans in secondNFA.getTransitions():
        trans['from'] = trans['from'] + maxLen
        idx = 0
        while idx < len(trans['to']):
            trans['to'][idx] = trans['to'][idx] + maxLen
            idx += 1
        newTransitions.append(trans)
    print(newTransitions)
    newAlpha = firstNFA.alphapet + list(set(secondNFA.alphapet) - set(firstNFA.alphapet))
    newNFA = NFA(firstNFA.initialState, len(newStates)-1,
                 newStates, newTransitions, newAlpha)
    print(newNFA)
    return newNFA


def kleeneStar(originalNFA):
    newStates = [0]
    addedStates = list(originalNFA.getStates())
    for state in np.add(addedStates, 1):
        newStates.append(state)
    newFinalState = len(originalNFA.getStates()) + 1
    newStates.append(newFinalState)

    newTransitions = []
    for trans in originalNFA.getTransitions():
        newTrans = {'to':[], 'tran': trans['tran']}
        newTrans['from'] = trans['from'] + 1
        idx = 0
        while idx < len(trans['to']):
            newTrans['to'].append(trans['to'][idx] + 1)
            idx += 1
        newTransitions.append(newTrans)
    newTransitions.append(
        {'from': 0, 'to': [newFinalState, originalNFA.initialState + 1], 'tran': ' '})
    newTransitions.append(
        {'from': originalNFA.finalState + 1, 'to': [originalNFA.initialState + 1, newFinalState], 'tran': ' '})
    
    newNFA = NFA(0, newFinalState, newStates, newTransitions, originalNFA.alphapet)
    return newNFA


def oneOrMore(originalNFA):
    kleeneNFA = kleeneStar(originalNFA)
    newNFA = concat(originalNFA, kleeneNFA)
    return newNFA


def union(firstNFA, secondNFA):
    newStates = [0]
    newTransitions = []
    maxLen = len(firstNFA.getStates()) + 1
    newFinalState = maxLen + len(secondNFA.getStates())
    for state in firstNFA.getStates():
        newStates.append(state+1)
    for state in secondNFA.getStates():
        newStates.append(state+maxLen)
    newStates.append(newFinalState)
    for trans in firstNFA.getTransitions():
        trans['from'] = trans['from'] + 1
        idx = 0
        while idx < len(trans['to']):
            trans['to'][idx] = trans['to'][idx] + 1
            idx += 1
        newTransitions.append(trans)

    for trans in secondNFA.getTransitions():
        trans['from'] = trans['from'] + maxLen
        idx = 0
        while idx < len(trans['to']):
            trans['to'][idx] = trans['to'][idx] + maxLen
            idx += 1
        newTransitions.append(trans)

    newTransitions.append(
        {'from': 0, 'to': [firstNFA.initialState + 1, secondNFA.initialState + maxLen], 'tran': ' '})
    newTransitions.append(
        {'from': firstNFA.finalState + 1, 'to': [newFinalState], 'tran': ' '})
    newTransitions.append(
        {'from': secondNFA.finalState + maxLen, 'to': [newFinalState], 'tran': ' '})
    
    newAlpha = firstNFA.alphapet + list(set(secondNFA.alphapet) - set(firstNFA.alphapet))
    newNFA = NFA(0, newFinalState, newStates, newTransitions, newAlpha)
    return newNFA


def questionMark(originalNFA):
    newStates = [0]
    for state in np.add(originalNFA.getStates(), 1):
        newStates.append(state)
    newFinalState = len(originalNFA.getStates()) + 1
    newStates.append(newFinalState)

    newTransitions = []
    for trans in originalNFA.getTransitions():
        trans['from'] = trans['from'] + 1
        idx = 0
        while idx < len(trans['to']):
            trans['to'][idx] = trans['to'][idx] + 1
            idx += 1
        newTransitions.append(trans)
    newTransitions.append(
        {'from': 0, 'to': [newFinalState, originalNFA.initialState + 1], 'tran': ' '})
    newTransitions.append(
        {'from': originalNFA.finalState + 1, 'to': [newFinalState], 'tran': ' '})

    newAlpha = originalNFA.alphapet
    newNFA = NFA(0, newFinalState, newStates, newTransitions, newAlpha)
    return newNFA


def postfixToNFA(postfix):
    nfaStack = stack()
    for char in postfix:
        if(isAlpha(char)):
            newNFA = NFA(0, 1, [0, 1], [{'from': 0, 'to': [1], 'tran': char}], [char])
            nfaStack.push(newNFA)
        elif char == '.':
            secondNFA = nfaStack.pop()
            newNFA = concat(nfaStack.pop(), secondNFA)
            nfaStack.push(newNFA)
        elif char == '*':
            newNFA = kleeneStar(nfaStack.pop())
            nfaStack.push(newNFA)
        elif char == '+':
            newNFA = oneOrMore(nfaStack.pop())
            nfaStack.push(newNFA)
        elif char == '|':
            secondNFA = nfaStack.pop()
            newNFA = union(nfaStack.pop(), secondNFA)
            nfaStack.push(newNFA)
        elif char == '?':
            newNFA = questionMark(nfaStack.pop())
            nfaStack.push(newNFA)
    return nfaStack.pop()

def extractNFA(regex):
    # regex = "(0|(1(01*(00)*0)*1)*)*"
    # regex = "(a|b)*abb(a|b)*"
    print("regex: ", regex)
    santReg = sanitaizeExpression(regex)
    print("sant mohab: ", santReg)

    postReg = infixToPostfix(santReg)
    print("postfix mohab: ", postReg)
    resultNFA = postfixToNFA(postReg)
    nfaString = str(resultNFA)
    ouptut_file = open("./" + "task_2_result.txt", "w+")
    ouptut_file.write(nfaString)

def openFile():
    parser = argparse.ArgumentParser(
        add_help=True, description='Sample Commandline')

    parser.add_argument('--file', action="store", help="path of file to take as input", nargs="?",
                        metavar="file")

    args = parser.parse_args()
    global fileName
    if(args.file):
        fileName = args.file
    input_file = open("./" + fileName, "r")
    for line in input_file:
        extractNFA(line)

if __name__ == '__main__':
    openFile()
    # postfix = infix_to_postfix(regex)
    # stack = transformToNFA(postfix)
