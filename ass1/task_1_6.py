import argparse
import re

fileName = "task1_6"
regexString = "[^(1|2|+)](?==)"


def printMatches():
    input_file = open("input/" + fileName+".txt", "r")
    ouptut_file = open("./" + fileName+"_result.txt", "w+")
    regex = re.compile(regexString)
    for line in input_file:
        matches = regex.findall(line)
        if(matches):
            for idx, match in enumerate(matches):
                newLine = "" if idx==len(matches)-1 else "\n"
                ouptut_file.write(match + newLine)


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
