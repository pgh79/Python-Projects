#Classing score
import os
import sys
import glob
import operator
class scorer:
    def __init__(self,file):
        
    def score(self,file):
        # Set the score to zero and open the file
        s = 0
        f = open(file, 'r')
        # Check each individual line
        for line in f.readlines():
            l = line.strip()
            # If the line stars with a comment, do nothing, else score it
            if l.startswith("#"):
                pass
            else:
                for char in line:
                    if char != ' ' and char != '\t' and char != '\n':
                        s += 1
                    if char == '\n':
                        s += 3
    def name(self,file):
        # Set the Name to blank
        n = ""
        f = open(file, 'r')
        linenum = 0
        for line in f.readlines():
            l = line.strip()
            linenum += 1
            # Check for comment, if line starts with comment then ignore.
            if linenum == 1:
                if l.startswith("#"):
                    # Ignore the hash and save the name
                    n = l[1:]
                else:
                    # No name means its invalid. Return an error message.
                    print 'You must include your name at the top in the form: #John Doe'
                    n = "No Name"
if __name__ == '__main__':
    p = sys.argv[1]
    if ".py" in p:
        print scorer(p).name + ': ',scorer(p).score
    else:
        print "dir"