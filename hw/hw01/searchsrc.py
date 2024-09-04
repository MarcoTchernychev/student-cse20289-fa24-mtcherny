#Marco Tchernychev
#mtcherny@nd.edu

import argparse
parser = argparse.ArgumentParser()
parser.add_argument("file", type=str)
parser.add_argument("--include", "--member", "--ptr", "--simplefunc", "--simplefuncec")
args = parser.parse_args()

filename = args.file

def readFile(filename):
    lines = []
    with open(filename, 'r') as f:
        for line in f:
            lines.append(line)
    return lines

lines = readFile(filename)
print(lines)

