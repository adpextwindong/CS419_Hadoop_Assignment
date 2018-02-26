#!/usr/bin/python

import sys

def mapper():
	dict = {}
	for line in sys.stdin:
		#print "DEBUG {0}".format(line)
		for word in line.split(" "):
			if word not in dict:
				dict[word] = 1;
			else:
				dict[word] = dict[word] + 1;
	for (key, val) in dict.items():
		print "{0}\t{1}".format(key, val)

if __name__ == "__main__":
	mapper()
