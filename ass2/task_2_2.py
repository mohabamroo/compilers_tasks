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
        printStr += ", ".join("q"+(str(x)) for x in self.states)
        printStr += "\n"
        printStr += ", ".join(str(x) for x in self.alphapet)
        printStr += "\n"
        printStr += (str(self.initialState) + "\n")
        printStr += (str(self.finalState) + "\n")
        printStr += ", ".join(("(" + x['from'] + ", " + x['trans'] +
                               ", " + x['to'] + ")") for x in self.transitions)
        printStr += "\n"
        return printStr


class DFA:
    def __init__(self, dfaTransitions, originalNFA):
        states_map = {}
        self.finalStates = []
        init_state_ord = ord('A')
        idx = 0
        # object with tuple keys, each key is a tuple of (sortedStatesTuple, symbol)
        for transition in dfaTransitions:
            set_of_states = transition[0]
            if set_of_states not in states_map:
                states_map[set_of_states] = chr(init_state_ord + idx)
                idx += 1
            if originalNFA.initialState in set_of_states:
                self.initialState = states_map[set_of_states]
            if originalNFA.finalState in set_of_states and states_map[set_of_states] not in self.finalStates:
                self.finalStates.append(states_map[set_of_states])
        self.transitions = [(states_map[trans[0]], trans[1], states_map[tuple(
            dfaTransitions[trans])]) for trans in dfaTransitions]
        self.states = [states_map[key] for key in states_map]
        self.alphapet = originalNFA.alphapet
        self.alphapet.remove(' ')

    def __str__(self):
        printStr = ""
        printStr += ", ".join((str(x)) for x in sorted(self.states))
        printStr += "\n"
        printStr += ", ".join(str(x) for x in sorted(self.alphapet))
        printStr += "\n"
        printStr += (self.initialState + "\n")
        printStr += ", ".join(str(x) for x in sorted(self.finalStates))
        printStr += "\n"
        printStr += ", ".join(str(x) for x in sorted(self.transitions))
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
        if(idx == 1):
            alphapet = line.strip().split(",")
            for (i, item) in enumerate(alphapet):
                if item == '':
                    alphapet[i] = ' '
            nfaDict['alphapet'] = alphapet
        if(idx == 2):
            initialState = line.strip()
            nfaDict['initialState'] = initialState
        if(idx == 3):
            finalState = line.strip()
            nfaDict['finalState'] = finalState
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


def getNFATransitions(nfa):
    new_nfa_transitions = {}
    # combine all transitions for each (state, symbol) pair in a single array
    # attach this array to a dict (like simple hashtable)
    for transition in nfa.transitions:
        try:
            new_nfa_transitions[(transition['from'], transition['trans'])].append(
                transition['to'])
        except:
            new_nfa_transitions[(transition['from'], transition['trans'])] = [
                transition['to']]
    return new_nfa_transitions


def convertNFATransToDFA(nfa_transition_table, dfa_states_set, nfaObj):
    new_dfa_transitions = {}
    for dfa_states in dfa_states_set:
        dfa_states = sorted(dfa_states)
        for char in nfaObj.alphapet:
            if char == ' ':
                continue
            destinations = []
            for state in dfa_states:
                indexTup = (state, char)
                if indexTup in nfa_transition_table:
                    for newDest in nfa_transition_table[indexTup]:
                        if newDest not in destinations:
                            destinations.append(newDest)
            final_destinations = []
            for dest in destinations:
                epsDestinations = epsilonClosure([dest], nfa_transition_table)
                for newEpsDest in epsDestinations:
                    final_destinations.append(newEpsDest)
            final_destinations = sorted(final_destinations)
            if(len(final_destinations) > 0):
                dfa_trans = (tuple(dfa_states), char)
                new_dfa_transitions[dfa_trans] = final_destinations
                dfa_states_tuple = tuple(final_destinations)

                if dfa_states_tuple not in dfa_states_set:
                    dfa_states_set.append(dfa_states_tuple)
            else:
                new_dfa_transitions[(tuple(dfa_states), char)] = ['DEAD']

    return new_dfa_transitions


def epsilonClosure(destinations, nfa_transition_table):
    for dest in destinations:
        indexTuple = (dest, ' ')
        if indexTuple in nfa_transition_table.keys():
            for newDest in nfa_transition_table[indexTuple]:
                if newDest not in destinations:
                    destinations.append(newDest)
    return sorted(destinations)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        add_help=True, description='Sample Commandline')

    parser.add_argument('--file', action="store", help="path of file to take as input", nargs="?",
                        metavar="file")

    args = parser.parse_args()
    if(args.file):
        fileName = args.file
    nfaObj = constructNFA()

    nfa_transition_table = getNFATransitions(nfaObj)

    dfa_initial = epsilonClosure([nfaObj.initialState], nfa_transition_table)

    dfa_transition_table = convertNFATransToDFA(
        nfa_transition_table, [tuple(dfa_initial)], nfaObj)

    final_dfa = DFA(dfa_transition_table, nfaObj)
    print(final_dfa)
    
    ouptut_file = open("./task_2_2_result.txt", "w+")
    ouptut_file.write(str(final_dfa))