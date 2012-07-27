#Scorer Interface
from scorer import *
import sys
script = sys.argv[1]
score = score(script)
name = str(name(script))
print "Challenge Score for " + name + " (Lower is Better): ", score