import argparse
import re

fileName = "task1_3"
regexString = "(aabb)"
# FIXME: my result has two more matches


def getLongestSequenceSize(search_str, polymer_str):
    matches = re.findall(r'(?:\b%s\b\s?)+' % search_str, polymer_str)
    longest_match = max(matches)
    return longest_match.count(search_str)


def printMatches():
    input_file = open("input/" + fileName+".txt", "r")
    ouptut_file = open("./" + fileName+"_result.txt", "w+")
    for line in input_file:
        matches =  re.findall(r"(?=((?:aabb|dc)+(?:aabb|dc)*))", line)
        if(matches):
            for idx, match in enumerate(matches):
                if(match != ''):
                    newLine = "" if idx==len(matches)-1 else "\n"
                    ouptut_file.write(match + newLine)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        add_help=True, description='Sample Commandline')

    parser.add_argument('--file', action="store", help="path of file to take as input", nargs="?",
                        metavar="file")

    args = parser.parse_args()
    if(args.file):
        fileName = args.file
    printMatches()
    regex = re.compile(regexString)
