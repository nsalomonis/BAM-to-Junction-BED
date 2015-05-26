### hierarchical_clustering.py
#Copyright 2005-2012 J. David Gladstone Institutes, San Francisco California
#Author Nathan Salomonis - nsalomonis@gmail.com

#Permission is hereby granted, free of charge, to any person obtaining a copy 
#of this software and associated documentation files (the "Software"), to deal 
#in the Software without restriction, including without limitation the rights 
#to use, copy, modify, merge, publish, distribute, sublicense, and/or sell 
#copies of the Software, and to permit persons to whom the Software is furnished 
#to do so, subject to the following conditions:

#THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, 
#INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A 
#PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT 
#HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION 
#OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE 
#SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

#################
### Imports an tab-delimited expression matrix and produces and hierarchically clustered heatmap
#################

# bugs, import matplotlib.colors as mc, -row_method
# new features fastcluster
import export
import string
import time
import sys, os
import shutil
import unique
import getopt
    
################# General data import methods #################

def filepath(filename):
    fn = unique.filepath(filename)
    return fn

def cleanUpLine(line):
    data = string.replace(line,'\n','')
    data = string.replace(data,'\c','')
    data = string.replace(data,'\r','')
    data = string.replace(data,'"','')
    return data
           
def getFolders(sub_dir):
    dir_list = unique.read_directory(sub_dir); dir_list2 = []
    ###Only get folder names
    for entry in dir_list:
        if '.' not in entry: dir_list2.append(entry)
    return dir_list2

def getFiles(sub_dir):
    dir_list = unique.read_directory(sub_dir); dir_list2 = []
    ###Only get folder names
    for entry in dir_list:
        if '.' in entry: dir_list2.append(entry)
    return dir_list2

def copyJunctionFiles(directory):
    
    root_dir = getFolders(directory)
    #print root_dir
    for top_level in root_dir: ### e.g., 
        try:
            files = getFiles(directory+'/'+top_level)
            for file in files:
                if 'junctions.bed' in file and 'junctionBEDfiles' not in top_level:
                    source_file = directory+'/'+top_level+'/'+file
                    source_file = filepath(source_file)
                    destination_file = directory+'/'+'junctionBEDfiles/'+top_level+'__junctions.bed'
                    destination_file = filepath(destination_file)
                    export.copyFile(source_file,destination_file)
                    print 'copying to:',destination_file
        except Exception:
            print 'failed to copy', source_file

if __name__ == '__main__':
    
    if len(sys.argv[1:])<=1:  ### Indicates that there are insufficient number of command-line arguments
        print "Warning! Please designate a BAM file as input in the command-line"
        print "Example: python BAMtoJunctionBED.py --i /Users/me/sample1.bam --g /Users/me/human.gtf"
        sys.exit()
    else:
        options, remainder = getopt.getopt(sys.argv[1:],'', ['i=','g=','r='])
        for opt, arg in options:
            if opt == '--i': directory=arg
    try: os.mkdir(directory+'/junctionBEDfiles')
    except Exception: pass
    copyJunctionFiles(directory)
    