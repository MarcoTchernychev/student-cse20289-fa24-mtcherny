#Marco Tchernychev
#mtcherny@nd.edu

import argparse
import subprocess
import os

#INPUT: string called filename that's from the command line
#OUTPUT: a list where each element is a string consisting of the contents of each line in filename 
def readFile(filename, path):
    lines = []
    with open(path+filename, 'r') as f:
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
        if line.count("::") == 1 and ";" not in line: #check for ";" to make sure it's really a function
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
        if "::" in lines[i] and i+3>len(lines): #check that there is a function present and that you will not read past list
            if "}" in lines[i+3] and lines[i].count("::")==1:
                count+=1
    return count

#INPUT: a list where each element is a string consisting of each line in a file
#OUTPUT: the number of times a function is called (with the first curly brace on its own line, or on the same line as the function name, and the last curly brace on a seperate line) that only has a single line of code or less
def countSimpleFuncEc(lines):
    count=0
    for i in range(len(lines)):
        if lines[i].count("::") == 1 and ";" not in lines[i]:
            if ("{" in lines[i] and "}" in lines[i+2]):
                count+=1
    return count

#Start of main
path = "../hw01/.gitignore/"
parser = argparse.ArgumentParser()
parser.add_argument("file", type=str)
parser.add_argument("--include", action="store_true")
parser.add_argument("--member", action="store_true")
parser.add_argument("--ptr", action="store_true")
parser.add_argument("--simplefunc", action="store_true")
parser.add_argument("--simplefuncec", action="store_true")
args = parser.parse_args()

filename = args.file
#path = subprocess.run(['where', filename], check=True).stdout.strip()
lines = readFile(filename, path)

print("file: "+str(filename))
print("path: "+path)
print("lines: "+str(len(lines)))
if args.include:
    print("include: "+str(countInclude(lines)))
if args.member:
    print("member: "+str(countMember(lines)))
if args.ptr:
    print("ptr: "+str(countPter(lines)))
if args.simplefunc:
    print("simplefunc: "+str(countSimpleFunc(lines)))
if args.simplefuncec:
    print("simplefuncec: "+str(countSimpleFuncEc(lines)))
