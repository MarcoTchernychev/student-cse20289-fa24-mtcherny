#Marco Tchernychev
#mtcherny@nd.edu

import argparse

#INPUT: string called filename that's from the command line
#OUTPUT: a list where each element is a string consisting of the contents of each line in filename 
def readFile(filename):
    lines = []
    with open(filename, 'r') as f:
        for line in f:
            lines.append(line)
    return lines

#INPUT: a list where each element is a string consisiting of each line in a file
#OUTPUT: the number of times an include statement is detected
def countInclude(lines):
    count = 0
    for line in lines:
        if "#include" in line:
            count+=1
    return count

#INPUT: a list where each element is a string consisiting of each line in a file
#OUTPUT: the number of times "::" is detected
def countMember(lines):
    count = 0
    for line in lines:
        if "::" in line:
            count+=1
    return count

#INPUT: a list where each element is a string consisiting of each line in a file
#OUTPUT: the number of times "->" is detected
def countPter(lines):
    count = 0
    for line in lines:
        if "->" in line:
            count+=1
    return count

#INPUT: a list where each element is a string consisiting of each line in a file
#OUTPUT: the number of times a function is called (with the first curly brace on its own line, and the last curly brace on a seperate line) that only has a single line of code or less
def countSimpleFunc(lines):
    count = 0
    for i in range(len(lines)):
        if "::" in lines[i] and "}" in lines[i+3]:
            count+=1
    return count

#INPUT: a list where each element is a string consisting of each line in a file
#OUTPUT: the number of times a function is called (with the first curly brace on its own line, or on the same line as the function name, and the last curly brace on a seperate line) that only has a single line of code or less
def countSimpleFuncEC(lines):
    count=0
    for i in range(len(lines)):
        if "::" in lines[i]:
            if ("{" in lines[i] and "}" in lines[i+2]) or ("{" in lines[i+3]):
                count+=1
    return count

#Start of main
parser = argparse.ArgumentParser()
parser.add_argument("file", type=str)
parser.add_argument("--include")
parser.add_argument("--member")
parser.add_argument("--ptr")
parser.add_argument("--simplefunc")
parser.add_argument("--simplefuncec")
args = parser.parse_args()
filename = args.file
lines = readFile(filename)
