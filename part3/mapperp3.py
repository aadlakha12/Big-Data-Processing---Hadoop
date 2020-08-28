#! /usr/bin/python3
 
from sys import stdin
import re
import os

for line in stdin:
	filename = os.environ["map_input_file"]
	part = filename.split('/');
	value = len(part)
	filename = part[value-1]
	line = line.strip()
	words = re.findall(r'\w+', line)
	for word in words:
		print(word.lower(), filename)
