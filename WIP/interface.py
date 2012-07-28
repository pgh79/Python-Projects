'''
Advanced Scorer Class
Using the argument after running the script, this will decide whether to run the directory scorer or single
file scorer.
CREDITS:
Directory Scorer - Blake Dutton
Single File Scorer - Patrick O'Connell, Peter Arnott, Blake Dutton
'''
import scorer
import os
import sys
import glob
import operator
def directory(path):
    #Create a dictionary to store all names and scores together
    dict = {}
    #List all of the files in the directory
    no = len([name for name in os.listdir('.') if os.path.isfile(name)])
    #For every file in the directory that ends in .py ...
    for infile in glob.glob( os.path.join(path, '*.py') ):
        #Ensure that infile is a string
        infile = str(infile)
        #Use the scorer and name methods in scorer.py
        score = scorer.score(infile)
        name = scorer.name(infile)
        #Store the values in the dictionary
        dict[score] = name
        #Print each value as its calculated
        print "Challenge Score for " + name + " (Lower is Better): ", score
    #Sort the dictionary in ascending order
    sorted_dict = sorted(dict.iteritems(), key=operator.itemgetter(0))
    #Open the leaderboard file and set a linenumber var to zero
    f = open('leaderboard.txt', 'w')
    linenum = 0
    #For each item in the sorted dictionary
    for item in sorted_dict:
        linenum += 1
        item = str(item)
        #If its the first line, dont add a newline, else add a new line
        if linenum == 1:
            f.write(item)
        else:
            f.write('\n' + item)
def onefile(script):
    #Perform the standard scoring script
    score = scorer.score(script)
    name = scorer.name(script)
    print "Challenge Score for " + name + " (Lower is Better): ", score
p = sys.argv[1]
if ".py" in p:
    onefile(p)
else:
    directory(p)
