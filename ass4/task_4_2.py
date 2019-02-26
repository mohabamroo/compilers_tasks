import argparse
import operator

output_filename="task_4_2_result.txt"

def extractRules(filename):
    input_file = open("./" + filename, "r")
    idx = -1
    rulesDictArr = []
    for line in input_file:
        colonSplitted = line.split(':')
        print(colonSplitted)
        ruleVar = colonSplitted[0].strip()
        ruleSubs = colonSplitted[1].split('|')
        ruleSubs = [x.strip() for x in ruleSubs]
        rulesDictArr.append({'var': ruleVar, 'sub': ruleSubs})
    print(rulesDictArr)
    return rulesDictArr

def applyLeftElimination(rulesArr):
    allResults = []
    for seperateRule in rulesArr:
        newRules = [seperateRule]
        idx = -1
        while True:
            idx += 1
            if idx >= len(newRules):
                break
            ruleObj = newRules[idx]
            ruleVar = ruleObj['var']
            ruleProds = ruleObj['sub']
            smallestFreq = {}
            for prod in ruleProds:
                if not prod == "epsilon":
                    try:
                        smallestFreq[prod[0]] += 1
                    except:
                        smallestFreq[prod[0]] = 1
            maxObj = max(smallestFreq.items(), key=operator.itemgetter(1))
            mostCommonChar = maxObj[0]
            maxValue = maxObj[1]
            if maxValue > 1 and not mostCommonChar == " ":
                newRuleVar = ruleVar + '\''
                newRules[idx]['newSubs'] = []
                newRules.append({'var': newRuleVar, 'sub': [], 'newSubs': []})
            else:
                break   
            for prod in ruleProds:
                if prod[0] == mostCommonChar:
                    x = 2
                    newProdOrig = prod[0] + " " + newRuleVar
                    if newProdOrig not in newRules[idx]['newSubs']:
                        newRules[idx]['newSubs'].append(newProdOrig)
                    newProd = prod[1:]
                    newRules[idx + 1]['sub'].append(newProd.strip())
                else:
                    newRules[idx]['newSubs'].append(prod.strip())
            print(mostCommonChar)
            print(smallestFreq)
        print(newRules)
        newRulesProccessed = []
        newIDx = -1
        for ruleObj in newRules:
            newIDx +=1
            if newIDx == len(newRules)-1:
                subs = ruleObj['sub']
            else:
                subs = ruleObj['newSubs']
            newRulesProccessed.append({'var': ruleObj['var'], 'sub': subs})
        allResults += newRulesProccessed
    return allResults

def writeResultFile(rulesArr):
    print("Final array")
    print(rulesArr)
    global output_filename
    ouptut_file = open("./" + output_filename, "w+")
    for ruleObj in rulesArr:
        newLine = ruleObj['var'] + ' : '
        newLine += " | ".join(ruleObj['sub'])
        newLine += "\n"
        ouptut_file.write(newLine)

if __name__ == '__main__':
    parser = argparse.ArgumentParser(add_help=True, description='Sample Commandline')

    parser.add_argument('--input-file', action="store", help="path of file to take as input to test strings in on DFA", nargs="?", metavar="input_file")
    
    args = parser.parse_args()
    rulesDictArr = extractRules(args.input_file)
    newRules = applyLeftElimination(rulesDictArr)
    writeResultFile(newRules)
