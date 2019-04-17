#!/usr/bin/env python3
import sys

# maps words to their counts
word2count = {}
 
# input comes from STDIN
for line in sys.stdin:
    # remove leading and trailing whitespace
    line = line.strip()
 
    # parse the input we got from mapper.py
    word, count = line.split('\t', 1)
    # convert count (currently a string) to int
    try:
        count = int(count)
    except ValueError:
        continue

    try:
        word2count[word] = word2count[word]+count
    except:
        word2count[word] = count
 
# write the tuples to stdout
for word, cnt in sorted(word2count.items(), key=lambda words: words[1], reverse = True):
    print('%s\t%s'% ( word, cnt ))
