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
        if line.count("::") == 1 and ";" not in line:
            count+=1
    return count

#INPUT: a list where each element is a string consisiting of each line in a file
#OUTPUT: the number of times "->" is detected
def countPter(lines):
    count = 0
    for line in lines:
        count+=line.count("->")
    return count

#INPUT: a list where each element is a string consisiting of each line in a file
#OUTPUT: the number of times a function is called (with the first curly brace on its own line, and the last curly brace on a seperate line) that only has a single line of code or less
def countSimpleFunc(lines):
    count = 0
    for i in range(len(lines)):
        if "::" in lines[i] and "}" in lines[i+3] and lines[i].count("::")==1:
            count+=1
    return count

#INPUT: a list where each element is a string consisting of each line in a file
#OUTPUT: the number of times a function is called (with the first curly brace on its own line, or on the same line as the function name, and the last curly brace on a seperate line) that only has a single line of code or less
def countSimpleFuncEc(lines):
    count=0
    for i in range(len(lines)):
        if lines[i].count("::") == 1 and ";" not in lines[i]:
            if ("{" in lines[i] and "}" in lines[i+2]): #or ("{" in lines[i+3]):
                count+=1
    return count

#Start of main
parser = argparse.ArgumentParser()
parser.add_argument("file", type=str)
parser.add_argument("--include", action="store_true")
parser.add_argument("--member", action="store_true")
parser.add_argument("--ptr", action="store_true")
parser.add_argument("--simplefunc", action="store_true")
parser.add_argument("--simplefuncec", action="store_true")
args = parser.parse_args()

filename = args.file
lines = readFile(filename)

print("file: "+str(filename)+" lines: "+str(len(lines)), end = " ")
if args.include:
    print("include: "+str(countInclude(lines)), end = " ")
if args.member:
    print("member: "+str(countMember(lines)), end = " ")
if args.ptr:
    print("ptr: "+str(countPter(lines)), end = " ")
if args.simplefunc:
    print("simplefunc: "+str(countSimpleFunc(lines)), end = " ")
if args.simplefuncec:
    print("simplefuncec: "+str(countSimpleFuncEc(lines)), end = " ")
print("")
