# Interface for scorer
import scorer
import os
import sys
import glob
import operator
def directory(path):
    dict = {}
    no = len([name for name in os.listdir('.') if os.path.isfile(name)])
    for infile in glob.glob( os.path.join(path, '*.py') ):
        infile = str(infile)
        y = scorer.score(infile)
        score = scorer.score(infile)
        name = scorer.name(infile)
        dict[score] = name
        print "Challenge Score for " + name + " (Lower is Better): ", score
    sorted_dict = sorted(dict.iteritems(), key=operator.itemgetter(0))
    f = open('leaderboard.txt', 'w')
    linenum = 0
    for item in sorted_dict:
        linenum += 1
        item = str(item)
        if linenum == 1:
            f.write(item)
        else:
            f.write('\n' + item)
def onefile(script):
    score = scorer.score(script)
    name = scorer.name(script)
    print "Challenge Score for " + name + " (Lower is Better): ", score
p = sys.argv[1]
if ".py" in p:
    onefile(p)
else:
    directory(p)
