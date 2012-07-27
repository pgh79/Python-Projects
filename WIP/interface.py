#Scorer Interface
import scorer
import sys
script = sys.argv[1]
score = scorer.score(script)
name = scorer.name(script)
print "Challenge Score for " + name + " (Lower is Better): ", score