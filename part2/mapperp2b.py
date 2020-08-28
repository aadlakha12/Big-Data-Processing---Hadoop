#! /usr/bin/python3

import sys
import string

for line in sys.stdin:
    line = line.strip()
    trigrams,count = line.split()
    print (trigrams,count)
