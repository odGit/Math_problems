# -*- coding: utf-8 -*-
"""
Created on Tue Oct  8 23:42:51 2013

@author: olgis

Problem:
    The series, 1**1 + 2**2 + 3**3 + ... + 10**10 = 10405071317.

    Find the last ten digits of the series, 1**1 + 2**2 + 3**3 + ... + 1000**1000.

"""
import time


limit = 1000
sum = 0

for i in xrange(1, limit):
        sum = sum + pow(i,i)

start = time.time()
product = str(sum)[-10:]
elapsed = time.time() - start

print "Last 10 digits is %s, found in %s sec." %(product, elapsed)
#Last 10 digits is 9110846700, found in 0.00121998786926 sec.