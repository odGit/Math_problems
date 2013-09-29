# -*- coding: utf-8 -*-
"""
Created on Thu Sep 26 21:48:04 2013

@author: olgis

By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, 
we can see that the 6th prime is 13.

PROBLEM: What is the 10 001st prime number?

"""
import time

def is_prime(x):
	x = abs(int(x))
	if x < 2:
		return False #"Less 2"
	elif x == 2:
		return True
	elif x % 2 == 0:
		return False	
	else:
		for n in range(3, int(x**0.5)+2, 2):
			if x % n == 0:
				return False
		return True

def look_for_prime(num):
    count = 0
    k = 1
    while count != num:
        if k < 3:
            k += 1
        else:
            k += 2
        if is_prime(k):
            count += 1
    return k
        
        
start = time.time()
product = look_for_prime(10001)
elapsed = time.time() - start

print "The 10 001st prime number is %s, found in %s sec" %(product, elapsed)