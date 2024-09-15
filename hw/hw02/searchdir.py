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

parser = argparse.ArgumentParser()
parser.add_argument("file", type=str)
parser.add_argument("path", type=str)
args = parser.parse_args()

print_dict(get_data(args.file, args.path))
