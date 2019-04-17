#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Mar 24 12:26:15 2019

@author: mohamadreza
"""
import sys
import re

# input comes from STDIN (standard input)
try:
    for line in sys.stdin:
        line = line.strip()
        words = line.split()
        for word in words:
            res = re.findall(r'\w+', word)
            for w in res:
                print('%s\t%s' % (w, 1))
except Exception as e:
    template = "An exception of type {0} occurred. Arguments:\n{1!r}"
    message = template.format(type(e).__name__, e.args)
    print(message)
    sys.exit(0)
