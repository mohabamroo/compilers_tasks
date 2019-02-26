import argparse

output_filename="task_4_1_result.txt"

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

def applyLeftRecursion(rulesArr):
	newRules = {}
	for ruleObj in rulesArr:
		ruleVar = ruleObj['var']
		newRules[ruleVar] = []
		newProds = []
		for prod in ruleObj['sub']:
			if prod[0] in newRules and not prod[0] == ruleVar:
				subProds = newRules[prod[0]]
				for subOpt in subProds:
					newProdStr = subOpt + prod[1:]
					newProds.append(newProdStr)
			else:
				# first token in production is not a variable
				newProds.append(prod)
			newProdsFiltered = []
			seenBefore = False
			newRuleVar = ruleVar + '\''
			for prod in newProds:
				if prod[0] == ruleVar:
					if not seenBefore:
						seenBefore = True
						newRules[newRuleVar] = ['epsilon']
					newRules[newRuleVar].append(prod[1:] + " " + newRuleVar)
				else:
					if seenBefore:
						prod = prod + " " + newRuleVar
					newProdsFiltered.append(prod)
			newRules[ruleVar] = newProdsFiltered
	return newRules

def writeResultFile(newRulesDict):
	global output_filename
	ouptut_file = open("./" + output_filename, "w+")
	for key in newRulesDict:
		newLine = key + ' : '
		newLine += " | ".join(newRulesDict[key])
		newLine += "\n"
		ouptut_file.write(newLine)

if __name__ == '__main__':
	parser = argparse.ArgumentParser(add_help=True, description='Sample Commandline')

	parser.add_argument('--input-file', action="store", help="path of file to take as input to test strings in on DFA", nargs="?", metavar="input_file")
	
	args = parser.parse_args()
	rulesDictArr = extractRules(args.input_file)
	newRules = applyLeftRecursion(rulesDictArr)
	writeResultFile(newRules)
