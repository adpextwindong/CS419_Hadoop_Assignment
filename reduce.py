#!/usr/bin/env/python

import sys

def reducer():
	dict = {}
	for line in sys.stdin:
		#print "LINE: ",line
		data = line.strip('\n').split("\t")
		if len(data) == 2:
			key, val = data
			#print "KEY: !{0}!".format(key)
			#print "VAL: ",val
		
			if key not in dict:
				#print "DEBUG {0}".format(key)
				dict[key] = val
			else:
				#print "ADDING !!!"
				dict[key].update({dict[key] + val})

	the_items = sorted(dict.items(), key=lambda x: int(x[1]), reverse=True)
	
	print "DEBUG " ,the_items
	for (k, v) in the_items:
		print "{0}\t{1}".format(k, v)

if __name__ == "__main__":
	reducer()
