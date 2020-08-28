#! /usr/bin/python3

import sys

word = None
tempword = None
tempcount = 0

result=[]
for line in sys.stdin:
	line =line.strip();
	word, countvalue = line.split(' ', 1)
	try:
		countvalue = int(countvalue)
	except ValueError:
		continue

	if tempword != word:
		if tempword:
			result.append([tempword, tempcount])
		tempcount = countvalue
		tempword = word
	else:
		tempcount = tempcount  + countvalue

if tempword == word:
	result.append([tempword, tempcount])
result.sort(key=lambda x:-x[1])

for i in result[0:10]:
	print(i[0],i[1])

