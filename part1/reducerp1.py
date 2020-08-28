#! /usr/bin/python3

import sys

worddict ={}

for line in sys.stdin:
	line =line.strip()
	word, count = line.split(' ', 1)
	try:
		count = int(count)
	except ValueError:
		continue

	if word not in worddict:
		worddict[word] = count
	else:
		worddict[word] = worddict[word] + count

for i in worddict:
	print(i,worddict[i])

