# -*- coding: utf-8 -*-
"""
Created on Thu Sep 26 21:48:04 2013

@author: olgis

The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

PROBLEM: Find the sum of all the primes below two million.

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
    k = 1
    primes = []
    while k < num:
        if is_prime(k):
            primes.append(k)
        if k < 3:
            k += 1
        else:
            k += 2
    return sum(primes)
        
        
start = time.time()
product = look_for_prime(2e6)
elapsed = time.time() - start

print "The sum of all the primes below two million is %s, found in %s sec" %(product, elapsed)
#The sum 142913828922 of all the primes below two million, found in 16.7116279602 sec