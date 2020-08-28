#!/usr/bin/python3

import sys

result ={};
l  = [None]*4
for line in sys.stdin:
	line = line.strip()
	EmployeeID, Name, Country, Salary, Passcode = line.split('\t')
	
	if EmployeeID not in result:
		result[EmployeeID] = l;
		if Name == '_':
			result[EmployeeID][1] = Salary
			result[EmployeeID][2] = Country
			result[EmployeeID][3] = Passcode
		else:
			result[EmployeeID][0] = Name 
	else:
		if Name == '_':
			result[EmployeeID][1] = Salary
			result[EmployeeID][2] = Country
			result[EmployeeID][3] = Passcode
		else:
			result[EmployeeID][0] = Name 
	l = [None]*4

for i in result:
	print(i, ", ".join(result[i]))
