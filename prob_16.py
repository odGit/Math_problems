# -*- coding: utf-8 -*-
"""
Created on Thu Sep 26 14:35:54 2013

@author: olgis

Problem: What is the sum of the digits of the number 2**1000?

"""

import time

def power_digit(a, p):
    sum = 0
    for letter in str(a ** p):
        sum += int(letter)
    return sum


start = time.time()
product = power_digit(2,1000)
elapsed = time.time() - start

print "The sum is %s, found in %s sec" % (product, elapsed)