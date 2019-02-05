import argparse
import re

fileName = "task1_5"
regexString = "((?<=(=))[0123456789]+)"


def printMatches():
    input_file = open("input/" + fileName+".txt", "r")
    ouptut_file = open("./" + fileName+"_result.txt", "w+")
    regex = re.compile(regexString)
    for line in input_file:
        matches = regex.findall(line)
        if(matches):
            for match in matches:
                ouptut_file.write(match[0] + "\n")


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