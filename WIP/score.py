#Classing score
import os
import sys
import glob
import operator
import re
class Scorer:
    def __init__(self,file):
        self.setscore(file)
        self.setname(file)
    def setscore(self,file):
        # Set the score to zero and open the file
        self.s = 0
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
                        self.s += 1
                    if char == '\n':
                        self.s += 3
    def setname(self,file):
        # Set the Name to blank
        self.n = ""
        f = open(file, 'r')
        linenum = 0
        for line in f.readlines():
            l = line.strip()
            linenum += 1
            # Check for comment, if line starts with comment then ignore.
            if linenum == 1:
                if l.startswith("#"):
                    # Ignore the hash and save the name
                    self.n = l[1:]
                else:
                    # No name means its invalid. Return an error message.
                    self.n = f.name
class Leaderboard:
    def __init__(self, path):
        self.dict = {}
        for infile in glob.glob( os.path.join(path, '*.py') ):
            infile = str(infile)
            score = Scorer(infile).s
            name = Scorer(infile).n
            self.dict[score] = name
            print name + ': ',score
            self.sort()
    def sort(self):
        self.sorted_dict = sorted(self.dict.iteritems(), key=operator.itemgetter(0))
    def output(self):
        f = open('Leaderboard.txt', 'w')
        linenum = 0
        for item in self.sorted_dict:
            linenum += 1
            item = str(item)
            item = re.sub(r'[^\w\s]', '', item)
            if linenum == 1:
                f.write(item)
            else:
                f.write('\n' + item)
if __name__ == '__main__':
    p = sys.argv[1]
    if ".py" in p:
        print Scorer(p).n + ': ', Scorer(p).s
    else:
        board = Leaderboard(p)
        board.output()
