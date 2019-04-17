#!/usr/bin/env python3
import sys

word2count = {}

for line in sys.stdin:
    line = line.strip()
    word, count = line.split('\t', 1)
    try:
        count = int(count)
    except ValueError:
        continue
    try:
        word2count[word] = word2count[word]+count
    except:
        word2count[word] = count

for word, cnt in sorted(word2count.items(), key=lambda words: words[1], reverse = True):
    print('%s\t%s'% ( word, cnt ))
