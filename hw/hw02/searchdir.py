#Marco Tchernychev
#mtcherny@nd.edu
import os
import subprocess
import argparse

#INPUT: file name and path
#OUTPUT: data from the specified file name and path in a dictionary {lines: ..., include: ..., etc}
def get_data(path, thefile):
    data = {} #dict to populated and returned
    file_path = os.path.join(path, thefile) #fusing path together
    result = subprocess.run(["python3", "searchsrc.py", file_path, "--include", "--includelocal", "--memberfuncs","--onelinefuncs"], stdout = subprocess.PIPE) #run searchsrc
    output = result.stdout.decode('utf-8') #make it a string
    line_list = output.split('\n') #split the lines
    line_list.remove('') #get rid of trailing empty string
    for line in line_list: #make each entry look as follows: [["path", "the path"],["file", "filename"],["lines","num of lines"], etc]
        data[line.split(': ')[0]] = line.split(': ')[1] #then immediately populate data dict as follows
    return data

#INPUT: dictionary
#OUTPUT: none, prints the dictionary in a compact way
def print_dict(data):
    print(f"{data['path']}, {data['file']}, {data['lines']} LOC, {data['include']} I, {data['includelocal']} LI, {data['memberfuncs']} MF, {data['onelinefuncs']} OLF")

#INPUT: path as a directory, flag denoting if output should be quiet (default is false), flag denoting if recursion is allowed (default is False)
#PURPOSE: scan directory in argument, invoke get_data so each file in dir has a dict, print pretty output for each file unless quiet arument is True
#OUTPUT: list of dicts with each file's data
def ScanDir(path, quiet = False, recursive = False):
    dict_list = [] #list to be popoulated with data from each dict
    for file in os.listdir(path):
        data_dict = get_data(path, file)
        dict_list.append(data_dict)
        if(quiet==False):
            print_dict(data_dict)
    return dict_list

parser = argparse.ArgumentParser()
parser.add_argument("file", type=str)
parser.add_argument("path", type=str)
parser.add_argument("-r", action="store_true", default = False, help = "denotes if directories should be processed recursively (default is false)")
parser.add_argument("--csv XXX", action="store_true", default = None, help = "an argument that also has a filename specified for the output (default is none)")
parser.add_argument("--stats", action="store_true", default = False, help = "denotes if stats should be computed across the numeric fields and reported (default is false)")
parser.add_argument("--quiet", action="store_true", default = False, help = "requests the output to stay quiet (no output of the pretty, compact one-line per file from Task 2) (default is False)")
args = parser.parse_args()

ScanDir("../hw01/src", args.quiet, args.r)
