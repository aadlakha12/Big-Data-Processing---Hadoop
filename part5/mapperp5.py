#! /usr/bin/python3

import sys
import math
import csv
import pandas as pd
import numpy as np

test =pd.read_csv('/home/cse587/Downloads/Test.csv')
test = test.to_numpy()

for lines in sys.stdin:
	lines = lines.strip()
	features = lines.split(",")
	#print(i)
	for i in range(len(test)):
		#print('tyes')
		
		value=0.0
		for j in range(len(features)-1):
			if features[j]!='':
				value += (float(features[j]) - float(test[i][j]))**2
				dist = math.sqrt(value)
		print(i,dist,features[len(features)-1])

