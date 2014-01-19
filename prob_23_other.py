# -*- coding: utf-8 -*-
"""
Created on Mon Dec 30 16:50:03 2013

@author: olgis

Find the sum of all the positive integers which cannot be 
written as the sum of two abundant numbers.
"""

#!/usr/bin/env python

import time

def sum_divisors(n):
    """Sums the proper divisors of n."""
    my_sum = 1
    for x in xrange(2, int(n ** 0.5) + 1):
        if (n % x == 0):
            my_sum += x + n / x
            
    if (n ** 0.5) == int(n ** 0.5):
        my_sum -= (n ** 0.5)
        
    return my_sum

def is_abundant(n):
    """Checks if the sum of the divisors of n is greater than n."""
    if sum_divisors(n) > n: 
        return True
    else: return False

def find_abundants(limit):
    """Finds all abundant numbers up to the specified limit"""
    abundants = [x for x in xrange(1, limit) if is_abundant(x)]
    return abundants

def get_list(limit):
    abds = find_abundants(limit)
    my_list = range(limit)
    for x in abds:
        for y in abds:
            if x + y >= limit:
                break
            my_list[x + y] = 0
    return my_list

start = time.time()
res = sum(get_list(28123))
elapsed = time.time() - start
print "The sum is %s, it took %s sec." %(res, elapsed)
