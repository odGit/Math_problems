# -*- coding: utf-8 -*-
"""
Created on Wed Oct  2 18:22:18 2013

@author: olgis

The Fibonacci sequence is defined by the recurrence relation:

    Fn = F_n−1 + F_n−2, where F1 = 1 and F2 = 1.

Hence the first 12 terms will be:

    F1 = 1
    F2 = 1
    F3 = 2
    F4 = 3
    F5 = 5
    F6 = 8
    F7 = 13
    F8 = 21
    F9 = 34
    F10 = 55
    F11 = 89
    F12 = 144

The 12th term, F12, is the first term to contain three digits.

What is the first term in the Fibonacci sequence to contain 1000 digits?
"""
import time

num_2 = 1
num_1 = 1 
count = 2
running = True

start = time.time()   
while running:
    res = num_1 + num_2
    if res < int(10**999):
        num_2 = num_1
        num_1 = res
        count +=1
    else:
        count +=1
        running = False
     
elapsed = time.time() - start

print "the first term in the Fibonacci sequence to contain 1000 digits is %s , found in %s sec"  %(count, elapsed)
#found in 0.00643587112427 sec
    