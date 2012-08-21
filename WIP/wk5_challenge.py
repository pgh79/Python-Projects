# Blake Dutton
import urllib2
i = open("input.txt", "r")
o = open("output.txt", "w")
for line in i.readlines():
	s = "http://finance.yahoo.com/d/quotes.csv?s=%s&f=j1" % line.strip()
	p = urllib2.urlopen(s)
	for l in p.readlines():
		out = line.strip() + " - " + l; o.write(out)