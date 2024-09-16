#Marco Tchernychev
#mtcherny@nd.edu
import os
import subprocess
import argparse
import csv
import statistics

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
    if recursive:
        for dirpath, _, filenames in os.walk(path): #use os.walk to recursively go through current directory and all subdirectories
            for file in filenames: #for each iteration above, access the filenames and its directory path for the directory that os.walk accessed
                data_dict = get_data(dirpath, file) #make the dictionary for the file
                dict_list.append(data_dict) #add it to the list
                if(quiet==False):
                    print_dict(data_dict) #print a pretty output if quiet argument is false
        if(len(dict_list)==0): #if dict_list is empty there was no directory so print that
            print("Directory does not exist or lacks source files")
            exit(1)
        return dict_list
    else:
        try: #try to run the for loop on the file given, if it doesn't work (except), print that the directory doesn't exist
            for file in os.listdir(path): #access all files under a directory
                data_dict = get_data(path, file)
                dict_list.append(data_dict)
                if(quiet==False):
                    print_dict(data_dict)
            return dict_list
        except:
            print("Directory does not exist or lacks source files")
            exit(1)

#INPUT: list of dicts
#PURPOSE: makes list of dicts into a csv file with the keys as the headers
#OUTPUT: a csv file to the specified file name in comand line arg
def ExtractCSV(csvName, dict_list):
    with open(csvName, mode='w', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=dict_list[0].keys()) #creating the objects making field names (headers) the keys
        writer.writeheader() #write the keys as the headers
        writer.writerows(dict_list) #write the rows (data)
    return csvName

#INPUT: list of dicts
#PURPOSE: makes a table where each field is a characteristic of a file (lines, include, etc) and each header is a statistic
#OUTPUT: a table that can be written to a .txt file called stats.txt
def getStats(dict_list):
    lines_list = []
    inc_list = []
    li_list = []
    mf_list = []
    olf_list = []
    name_list = []
    for dict in dict_list: #make a list containing all of the values under the dictionary keys
        lines_list.append(int(dict['lines']))
        inc_list.append(int(dict['include']))
        li_list.append(int(dict['includelocal']))
        mf_list.append(int(dict['memberfuncs']))
        olf_list.append(int(dict['onelinefuncs']))
        name_list.append(dict['file'])
    with open('stats.txt', 'w') as file: #using f strings write to stats.txt all the statistics required
        file.write("Field, Min, MinFile, Max, MaxFile, Mean, Median, StdDev \n")
        file.write(f"lines, {min(lines_list)}, {name_list[lines_list.index(min(lines_list))]}, {max(lines_list)}, {name_list[lines_list.index(max(lines_list))]}, {statistics.mean(lines_list)}, {statistics.median(lines_list)}, {statistics.stdev(lines_list):.1f}\n")
        file.write(f"includes, {min(inc_list)}, {name_list[inc_list.index(min(inc_list))]}, {max(inc_list)}, {name_list[inc_list.index(max(inc_list))]}, {statistics.mean(inc_list)}, {statistics.median(inc_list)}, {statistics.stdev(inc_list):.1f}\n")
        file.write(f"localincludes, {min(li_list)}, {name_list[li_list.index(min(li_list))]}, {max(li_list)}, {name_list[li_list.index(max(li_list))]}, {statistics.mean(li_list)}. {statistics.median(li_list)}, {statistics.stdev(li_list):.1f}\n")
        file.write(f"memberfuncs, {min(mf_list)}, {name_list[mf_list.index(min(mf_list))]}, {max(mf_list)}, {name_list[mf_list.index(max(mf_list))]}, {statistics.mean(mf_list)}, {statistics.median(mf_list)}, {statistics.stdev(mf_list):.1f}\n")
        file.write(f"onelinefuncs, {min(olf_list)}, {name_list[olf_list.index(min(olf_list))]}, {max(olf_list)}, {name_list[olf_list.index(max(olf_list))]}, {statistics.mean(olf_list)}, {statistics.median(olf_list)}, {statistics.stdev(olf_list):.1f}")

parser = argparse.ArgumentParser()
parser.add_argument("--file", type=str)
parser.add_argument("path", type=str)
parser.add_argument("-r", action="store_true", default = False, help = "denotes if directories should be processed recursively (default is false)")
parser.add_argument("--csv", type=str, default = None, help = "an argument that also has a filename specified for the output (default is none)")
parser.add_argument("--stats", action="store_true", default = False, help = "denotes if stats should be computed across the numeric fields and reported (default is false)")
parser.add_argument("--quiet", action="store_true", default = False, help = "requests the output to stay quiet (no output of the pretty, compact one-line per file from Task 2) (default is False)")
args = parser.parse_args()
if not args.path:
    print("Make sure you specify a directory to scan")
    exit(1)
if not args.csv:
    print("Make sure you specify the name of the csv file to write to")
    exit(1)

dict_list = ScanDir(args.path, args.quiet, args.r)
ExtractCSV(args.csv,dict_list)

if(args.stats):
    getStats(dict_list)
