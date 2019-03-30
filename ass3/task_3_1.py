import argparse

output_filename = 'task_3_1_result.txt'
# implemented from one line input only as stated in the tutorial

class DFA:
    def __init__(self, dfaDict):
        states_map = {}
        self.finalStates = dfaDict['finalStates']
        self.initialState = dfaDict['initialState']
        self.transitions = dfaDict['transitions']
        self.transitionsMap = {}
        for transition in self.transitions:
            self.transitionsMap[(transition['from'], transition['trans'])] = transition['to']
        self.states = dfaDict['states']
        self.alphapet = dfaDict['alphapet']
        self.actions = dfaDict['actions']
        self.labels = dfaDict['labels']
        self.stateActionMap = {}
        for state in self.labels:
            label = self.labels[state]
            action = self.actions[label]
            self.stateActionMap[state] = action

class Stack:
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

    def length(self):
        return len(self.array)

def constructDFA(fileName):
    input_file = open("./" + fileName, "r")
    idx = -1
    dfaDict = {}
    for line in input_file:
        idx += 1
        if(idx == 0):
            states = line.strip().split(",")
            dfaDict['states'] = states
        if(idx == 1):
            alphapet = line.strip().split(",")
            dfaDict['alphapet'] = alphapet
        if(idx == 2):
            initialState = line.strip()
            dfaDict['initialState'] = initialState
        if(idx == 3):
            line = line.replace(' ', '')
            finalStates = line.strip().split(',')
            dfaDict['finalStates'] = finalStates
        if(idx == 4):
            dfaDict['transitions'] = []
            line = line.strip()
            line = line.replace(', ,', ',*,')
            line = line.replace(' ', '')
            transitions = line.split('),(')
            for (i, item) in enumerate(transitions):
                transitions[i] = transitions[i].replace('(', '')
                transitions[i] = transitions[i].replace(')', '')
                transitions[i] = transitions[i].replace('*', ' ')
                transitions[i] = transitions[i].split(',')
                dfaDict['transitions'].append(
                    {'from': transitions[i][0], 'to': transitions[i][2], 'trans': transitions[i][1]})
        if(idx == 5):
            dfaDict['labels'] = {}
            line = line.strip()
            line = line.replace(', ,', ',*,')
            line = line.replace(' ', '')
            line = line.replace('"', '')
            labels = line.split('),(')
            for (i, item) in enumerate(labels):
                labels[i] = labels[i].replace('(', '')
                labels[i] = labels[i].replace(')', '')
                labels[i] = labels[i].split(',')
                dfaDict['labels'][labels[i][0]] = labels[i][1]
        if(idx == 6):
            dfaDict['actions'] = {}
            line = line.strip()
            line = line.replace(', ,', ',*,')
            line = line.replace('), (', '),(')
            line = line.replace('"', '')
            actions = line.split('),(')
            for (i, item) in enumerate(actions):
                actions[i] = actions[i].replace('(', '')
                actions[i] = actions[i].replace(')', '')
                actions[i] = actions[i].split(',')
                dfaDict['actions'][actions[i][0]] = actions[i][1]
    return DFA(dfaDict)

def fallbackDFA(dfa, string):
    startIdx = 0
    reallyDead = False
    strignToReturn = ""
    while startIdx < len(string) and not reallyDead: 
        statesStack = Stack()
        newStr = string[startIdx:]
        statesStack.push(dfa.initialState)
        for char in newStr:
            currentState = statesStack.top()
            newState = dfa.transitionsMap[(statesStack.top(), char)]
            statesStack.push(newState)
        while not statesStack.empty():
            popState = statesStack.pop()
            if(popState in dfa.finalStates):
                oldStartIdx = startIdx
                startIdx = statesStack.length()
                strignToReturn = strignToReturn + string[oldStartIdx:startIdx] + ", \"" + dfa.stateActionMap[popState].strip() + "\"\n"
                break
        if(statesStack.empty()):
            reallyDead = True
            strignToReturn = strignToReturn + string[startIdx:] + ", \"" + dfa.stateActionMap[dfa.initialState].strip() + "\"\n"
            break
    return strignToReturn

def applyActions(dfa, fileName):
    string_file = open("./" + fileName, "r")
    outputString = ""
    ouptut_file = open("./" + output_filename, "w+")
    for line in string_file:
        stringToMatch = line.strip()
        resString = fallbackDFA(dfa, stringToMatch)
        outputString += resString
    ouptut_file.write(outputString)

if __name__ == '__main__':
    parser = argparse.ArgumentParser(add_help=True, description='Sample Commandline')

    parser.add_argument('--dfa-file', action="store", help="path of file to take as input to construct DFA", nargs="?", metavar="dfa_file")
    parser.add_argument('--input-file', action="store", help="path of file to take as input to test strings in on DFA", nargs="?", metavar="input_file")
    
    args = parser.parse_args()
    dfaObj = constructDFA(args.dfa_file)
    applyActions(dfaObj, args.input_file)

