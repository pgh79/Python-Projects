''' 

Code Challenge Scorer: Lower is Better
-> Whitespace (' ') is ignored
-> Tabs are ignored
-> Newlines count for THREE POINTS (v. Bad)

How to Use:
Place this file inside the directory that contains your challenge solution. Then run python scorer.py <solution.py> where solution.py is what you named your challenge solution.

Credits: Pocon, Peterarenot, Blakedut2

'''
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
        self.score = 0
        f = open(file, 'r')
        for line in f.readlines():
            l = line.strip()
            if not l.startswith("#"):
                if not "input" in l:
                    for char in line:
                        if char != ' ' and char != '\t' and char != '\n':
                            self.score += 1
                        if char == '\n':
                            pass
    def setname(self,file):
        f = open(file, 'r')
        linenum = 0
        for line in f.readlines():
            l = line.strip()
            linenum += 1
            if linenum == 1:
                if l.startswith("#"):
                    self.name = l[1:]
                else:
                    self.name = f.name
class Leaderboard:
    def __init__(self, path):
        self.scorelist = []
        for infile in glob.glob( os.path.join(path, '*.py') ):
            self.scorelist += [Scorer(infile)]
        self.sort()
    def sort(self):
        self.sorted = sorted(self.scorelist, key=lambda score: score.score)
    def output(self):
        f = open('Leaderboard.md', 'w')
        linenum = 0
        for item in self.scorelist:
            linenum += 1
            if linenum == 1:
                f.write('Leaderboard')
                f.write('\n===========')
            else:
                f.write('\n' + str(item.score) + ": " + item.name)
if __name__ == '__main__':
    p = sys.argv[1]
    if ".py" in p:
        print Scorer(p).name + ': ', Scorer(p).score
    else:
        board = Leaderboard(p)
        board.output()
