#Marco Tchernychev
#mtcherny@nd.edu
import argparse
import re

#INPUT: string called filename that's from the command line
#OUTPUT: a list where each element is a string consisting of the contents of each line in filename 
def readFile(filename):
    #ccfile = re.compile(r'$.cc')
    #mo = ccfile.search(filename)
    #print("YO: "+filename)
    #if mo:
    lines = []
        #with open(filename, 'r') as f:
    with open(filename, 'r', encoding='utf-8', errors='ignore') as f:
        for line in f:
            lines.append(line)
    
    return lines

#INPUT: a list where each element is a string consisiting of each line in a file
#OUTPUT: the number of times an include statement is detected
def countInclude(lines):
    count = 0
    for line in lines:
        if line.startswith("#include"):
            count+=1
    return count

#INPUT: a list where each element is a string consisiting of each line in a file
#OUTPUT: the number of times a local include statemnt is added (using  "", not <>)
def countIncludeLocal(lines):
    locinc = re.compile(r'^#include ".*"')
    count = 0
    for line in lines:
        mo = locinc.search(line)
        if mo:
            count+=1
    return count

#INPUT: a list where each element is a string consisiting of each line in a file
#OUTPUT: the number of times "::" is detected
def countMemberFuncs(lines):
    memfunc = re.compile(r'^[a-zA-Z0-9].*::.*')
    count = 0
    for line in lines:
        mo = memfunc.search(line)
        if mo:
            count+=1
    return count

#INPUT: a list where each element is a string consisiting of each line in a file
#OUTPUT: the number of times a function is called (with the first curly brace on its own line, and the last curly brace on a seperate line) that only has a single line of code or less
def countOneLineFuncs(lines):
    OLF1 = re.compile(r'^[a-zA-Z0-9].*::.*')
    OLF2 = re.compile(r'\{') 
    OLF3 = re.compile(r'.*')
    OLF4 = re.compile(r'\}')
    count = 0
    for i in range(len(lines)):
        if i+2<len(lines): #check that there is a function present and that you will not read past list
            if OLF1.search(lines[i]) and OLF2.search(lines[i+1]) and OLF3.search(lines[i+2]) and OLF4.search(lines[i+3]):
                count+=1
    return count

#Start of main
parser = argparse.ArgumentParser()
parser.add_argument("file", type=str)
parser.add_argument("--include", action="store_true")
parser.add_argument("--includelocal", action="store_true")
parser.add_argument("--memberfuncs", action="store_true")
parser.add_argument("--onelinefuncs", action="store_true")
args = parser.parse_args()

filename = args.file
lines = readFile(filename)

print("path: " + str(filename).rsplit('/',1)[0]+'/')
print("file: "+str(filename).split('/')[-1])
print("lines: "+str(len(lines)))
if args.include:
    print("include: "+str(countInclude(lines)))
if args.includelocal:
    print("includelocal: "+str(countIncludeLocal(lines)))
if args.memberfuncs:
    print("memberfuncs: "+str(countMemberFuncs(lines)))
if args.onelinefuncs:
    print("onelinefuncs: "+str(countOneLineFuncs(lines)))
