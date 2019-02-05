import argparse
import re

fileName = "task1_2"
regexString = "(aabb)"


def getLongestSequenceSize(search_str, polymer_str):
    matches = re.findall(r'(?:\b%s\b\s?)+' % search_str, polymer_str)
    print('TCL: matches', matches)
    longest_match = max(matches)
    print ('TCL: longest_match' + longest_match)
    return longest_match.count(search_str)


def printMatches():
    input_file = open("input/" + fileName+".txt", "r")
    ouptut_file = open("./" + fileName+"_result.txt", "w+")
    for line in input_file:
        matches =  re.findall(r"(?=((?:aabb)+(?:aabb)*))", line)
        matches = 
        print matches
        if(matches):
            for match in matches:
                if(match != ''):
                    ouptut_file.write(match + "\n")


if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        add_help=True, description='Sample Commandline')

    parser.add_argument('--file', action="store", help="path of file to take as input", nargs="?",
                        metavar="file")

    args = parser.parse_args()
    print("Printing args..")
    if(args.file):
        fileName = args.file
    print(args.file)
    printMatches()
    regex = re.compile(regexString)
