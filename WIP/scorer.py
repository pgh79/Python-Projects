''' 

Code Challenge Scorer: Lower is Better
-> Whitespace (' ') is ignored
-> Tabs are ignored
-> Newlines count for THREE POINTS (v. Bad)

How to Use:
Place this file inside the directory that contains your challenge solution. Then run python scorer.py <solution.py> where solution.py is what you named your challenge solution.

'''
import sys
class scorer:
    def score(file):
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
        return s
    def name(file):
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
        return n
