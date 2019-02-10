import argparse

fileName = "task_2_2_input"


class NFA:
    def __init__(self, nfaDict):
        self.initialState = nfaDict['initialState']
        self.finalState = nfaDict['finalState']
        self.states = nfaDict['states']
        self.alphapet = nfaDict['alphapet']
        self.transitions = nfaDict['transitions']

    def __str__(self):
        printStr = ""
        # printStr += "States:\n"
        printStr += ",".join("q"+(str(x)) for x in self.states)
        printStr += "\n"
        # printStr += "Alpha:\n"
        printStr += ",".join(str(x) for x in self.alphapet)
        printStr += "\n"
        printStr += (str(self.initialState) + "\n")
        printStr += (str(self.finalState) + "\n")
        # printStr += "transitions:\n"
        printStr += ", ".join(("(" + x['from'] + ", " + x['trans'] +
                               ", " + x['to'] + ")") for x in self.transitions)
        printStr += "\n"
        return printStr


def constructNFA():
    input_file = open("./" + fileName+".txt", "r")
    idx = -1
    nfaDict = {}
    for line in input_file:
        idx += 1
        if(idx == 0):
            states = line.strip().split(",")
            nfaDict['states'] = states
            print(states)
        if(idx == 1):
            alphapet = line.strip().split(",")
            for (i, item) in enumerate(alphapet):
                if item == '':
                    alphapet[i] = ' '
            nfaDict['alphapet'] = alphapet
            print(alphapet)
        if(idx == 2):
            initialState = line.strip()
            nfaDict['initialState'] = initialState
            print(initialState)
        if(idx == 3):
            finalState = line.strip()
            nfaDict['finalState'] = finalState
            print(finalState)
        if(idx == 4):
            nfaDict['transitions'] = []
            line = line.replace(', ,', ',*,')
            line = line.replace(' ', '')
            transitions = line.split('),(')
            for (i, item) in enumerate(transitions):
                transitions[i] = transitions[i].replace('(', '')
                transitions[i] = transitions[i].replace(')', '')
                transitions[i] = transitions[i].replace('*', ' ')
                transitions[i] = transitions[i].split(',')
                nfaDict['transitions'].append(
                    {'from': transitions[i][0], 'to': transitions[i][2], 'trans': transitions[i][1]})
            # print(transitions)
    return NFA(nfaDict)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        add_help=True, description='Sample Commandline')

    parser.add_argument('--file', action="store", help="path of file to take as input", nargs="?",
                        metavar="file")

    args = parser.parse_args()
    print("Printing args..")
    if(args.file):
        fileName = args.file
    print("File " + fileName)
    nfaObj = constructNFA()
    print(nfaObj)
