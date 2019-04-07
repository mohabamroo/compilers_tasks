import argparse

output_filename = 'task_5_1_result.txt'
# Use "input-file" argument to pass the full name of input file (with extension)
# This code doesn't handle <'> in the tokens, you can't use <E'> for example
# Follow and First reference:
# https://www.geeksforgeeks.org/compiler-design-follow-set-in-syntax-analysis/
# FIXME: test case 6, 9
def isAlpha(char):
    return not char.isupper()

def getFirst(var, dfaDict):
    ruleProds = dfaDict[var]
    firstSet = []
    for prod in ruleProds:
        if prod == "epsilon":
            firstSet.append(prod)
        elif prod[0].isupper():
            idx = 1
            newFirsts = getFirst(prod[0], dfaDict)
            for newChar in newFirsts:
                if not newChar == 'epsilon':
                    firstSet.append(newChar)
            while idx < len(prod):
                if 'epsilon' in newFirsts and prod[idx].isupper():
                    newFirsts = getFirst(prod[idx], dfaDict)
                    for newChar in newFirsts:
                        if not newChar == 'epsilon':
                            firstSet.append(newChar)
                idx += 1
        elif isAlpha(prod[0]):
            firstSet.append(prod[0])
    uniqueFirst = []
    for char in firstSet:
        if not char in uniqueFirst:
            uniqueFirst.append(char)
    return uniqueFirst

def getFollow(var, dfaDict, newRules, flag = False):
    followSet = []
    if flag:
        followSet.append('$')
    for rule in dfaDict:
        for prod in dfaDict[rule]:
            for idx, char in enumerate(prod):
                if char == var and not rule == var:
                    if idx + 1 == len(prod):
                        followSet = getFollow(rule, dfaDict, newRules)
                    else:
                        newIdx = idx + 1
                        while newIdx < len(prod):
                            followingChar = prod[newIdx]
                            # print(var, "followed by: ", followingChar)
                            if followingChar.isupper():
                                subFollow = newRules[followingChar]['first']
                                followSet += subFollow
                                if not 'epsilon' in subFollow:
                                    break
                                elif newIdx + 1 == len(prod):
                                    subFollow = getFollow(rule, dfaDict, newRules)
                                    followSet += subFollow
                            elif isAlpha(followingChar):
                                followSet.append(followingChar)
                                break
                            newIdx += 1
    uniqueFollow = []
    for c in followSet:
        if not c == 'epsilon' and not c in uniqueFollow:
            uniqueFollow.append(c)
    if len(uniqueFollow) == 0:
        uniqueFollow.append('$')
    return uniqueFollow

def constructDFA(fileName):
    # reading file and processing input in a productions dictionary
    input_file = open("./" + fileName, "r")
    idx = -1
    dfaDict = {}
    alpha = []
    orderedRules = []
    for line in input_file:
        ruleStr = line.strip().split(":")
        ruleVar = ruleStr[0].strip()
        ruleProds = ruleStr[1].split('|')
        orderedRules.append(ruleVar)
        dfaDict[ruleVar] = [prod.strip().replace(' ', '') for prod in ruleProds]
    
    print(orderedRules)

    # applying the getFirst on all rules
    newRules = {}
    for idx, rule in enumerate(orderedRules):
        newRules[rule] = {}
        newRules[rule]['first'] = getFirst(rule, dfaDict)

    # applying get follow on all rules
    for idx, rule in enumerate(orderedRules):
        flag = False
        if(idx == 0):
            flag = True
        newRules[rule]['follow'] = getFollow(rule, dfaDict, newRules, flag)

    print(dfaDict)
    print("\n")

    # constructing the output string in needed format
    outputStr = ''
    for rule in orderedRules:
        outputStr = outputStr + rule + ' : '
        outputStr += ' '.join(newRules[rule]['first'])
        outputStr += ' : '
        outputStr += ' '.join(newRules[rule]['follow'])
        outputStr += "\n"

    # writing to ouptut file
    global output_filename
    ouptut_file = open("./" + output_filename, "w+")
    ouptut_file.write(outputStr)

    print(outputStr)
    
if __name__ == '__main__':
    parser = argparse.ArgumentParser(add_help=True, description='Sample Commandline')

    parser.add_argument('--input-file', action="store", help="path of file to take as input to test strings in on DFA", nargs="?", metavar="input_file")
    args = parser.parse_args()
    dfaObj = constructDFA(args.input_file)

