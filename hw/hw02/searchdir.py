#Marco Tchernychev
#mtcherny@nd.edu
import os
import subprocess
import searchsrc

#INPUT: file name and path
#OUTPUT: data from the specified file name and path in a dictionary {lines: ..., include: ..., etc}
def get_data(path, file):
    data = {} #dict to populated and returned
    file_path = os.path.join(path, file) #fusing path together
    result = subprocess.run(["python3", "searchsrc.src", file_path, "--include", "--includelocal", "--memberfuncs","--onelinefuncs"]) #run searchsrc
    line_list = result.stdout.splitlines() #gives back a list where each elemenet is the sring of each line that searchsrc returns
    for line in line_list: #make each entry look as follows: [["path", "the path"],["file", "filename"],["lines","num of lines"], etc]
        dict[line.split(': ')[0]] = line.split[1] #then immediately populate data dict as follows
    return data

#INPUT: dictionary
#OUTPUT: none, prints the dictionary is a compact way
def print_dict(data):
    print(f"{data['path']}, {data['file']}, {data['lines']} LOC, {data['include']} I, {data['includelocal']} LI, {data['memberfuncs']} MF, {data['onelinefuncs']} OLF")
