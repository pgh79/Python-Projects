#Leaderboard
import scorer
import os
import sys
import glob
scorelist = []
namelist = []
no = len([name for name in os.listdir('.') if os.path.isfile(name)])
path = sys.argv[1]
for infile in glob.glob( os.path.join(path, '*.py') ):
    infile = str(infile)
    scorelist[1:1] = scorer.score(infile)
    namelist[1:1] = scorer.name(infile)
    print "Challenge Score for " + name + " (Lower is Better): ", score
    