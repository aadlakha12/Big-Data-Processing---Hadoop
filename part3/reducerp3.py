#! /usr/bin/python3

from sys import stdin

worddict={}

for line in stdin:
	line = line.strip()
	word,filename = line.split(' ')	
	if word not in worddict:
		worddict[word] = []
		worddict[word].append(filename)
	else:
		if filename not in worddict[word]:
			worddict[word].append(filename)

for i in worddict:
	print(i, ', '.join(worddict[i]))
