#! /usr/bin/python3

import sys

keys=[];
table={};
for line in sys.stdin:
	line= line.strip()
	features=line.split()
	if features[0] not in keys:
		keys.append(features[0])
		table[features[0]] =[[float(features[1]),int(features[2])]]
		
	elif features[0] in table.keys():
		table[features[0]].append([float(features[1]),int(features[2])])

K=3
result ={};
for i in sorted(table.keys()):
	#table[i].sort(key=lambda x:x[0])
	#lables=[]	
	#for j in range(K):
	#	lables.append(table[i][j][1])
	#result[int(i)] = mode(lables)
	word_counter = {}
	for word in table[i]:
		value ={'count':0,'distance':0}
		if word[0] in word_counter:
			word_counter[word[0]]['count'] =  word_counter[word[0]]['count'] + 1
			word_counter[word[0]]['distance'] = word_counter[word[0]]['distance'] + word[0]
		else:
			value['count']=1
			value['distance'] =word[0]
			word_counter[word[1]] = value
			values = sorted(word_counter.items(), key=lambda x: (x[1]['count'],-x[1]['distance']), reverse=True)
		result[int(i)] =values[0][0]

#print(result)
for i in sorted(result.keys()):
	print(i,result[i])
	


