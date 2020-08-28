#! /usr/bin/python3

import sys;
list_trigrams=[]
words=[]
import nltk
nltk.download('punkt')
from nltk.stem import PorterStemmer
from nltk.tokenize import word_tokenize
ps = PorterStemmer();
for line in sys.stdin:
    line = line.strip()
    line_words = line.split()
    words.extend(line_words)

n=0

for l in words:
    try:
        if ('science' in ps.stem(l) or 'sea' in ps.stem(l) or 'fire' in ps.stem(l)) and n==0: 
            list_trigrams.append("$_%s_%s " % (words[n+1], words[n+2]))

        elif ('science' in ps.stem(l) or 'sea' in ps.stem(l) or 'fire' in ps.stem(l)) and n==1: 
            list_trigrams.extend(["%s_$_%s" % (words[n-1], words[n+1]),"$_%s_%s" % (words[n+1], words[n+2])]) 

        elif ('science' in ps.stem(l) or 'sea' in ps.stem(l) or 'fire' in ps.stem(l)):
            list_trigrams.append("%s_%s_$" % (words[n-2], words[n-1]))
            list_trigrams.append("%s_$_%s" % (words[n-1], words[n+1]))
            list_trigrams.append("$_%s_%s" % (words[n+1], words[n+2])) 
                   
    except:
        continue
        
    n=n+1

for ngram in list_trigrams:     
    print(ngram, 1);
