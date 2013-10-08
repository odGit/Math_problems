# -*- coding: utf-8 -*-
"""
Created on Tue Oct  8 23:55:12 2013

@author: olgis

Problem:
    Considering natural numbers of the form, ab, where a, b < 100,
     what is the maximum digital sum?
"""

max_sum = 0

for a in xrange(1,100):
    for b in xrange(1,100):
        res = str(a**b)
        digits = [int(digit) for digit in res]
        q = sum(digits)
        if q > max_sum:
            max_sum = q

print max_sum