#!/usr/bin/python3

import sys

for line in sys.stdin:
	line = line.strip()
	line1 = line.split("\t")
	EmployeeID = "_"
	Name = "_"
	Passcode = "_"
	Salary = "_"
	Country = "_"
	if(len(line1)) ==2:
		EmployeeID = line1[0] 
		Name = line1[1]
	else:
		EmployeeID = line1[0]
		Salary = line1[1]
		Country = line1[2]
		Passcode = line1[3]
	if EmployeeID == 'Employee ID':
		continue;	
	print (EmployeeID+"\t"+Name +"\t"+Country+"\t"+Salary+"\t"+Passcode)

