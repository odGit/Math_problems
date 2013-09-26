# -*- coding: utf-8 -*-
"""
Created on Thu Sep 26 14:35:54 2013

@author: olgis

Problem: A palindromic number reads the same both ways. The largest palindrome
made from the product of two 2-digit numbers is 9009 = 91 × 99.

Find the largest palindrome made from the product of two 3-digit numbers.

"""
import time

def is_palindromic(num):
    str_num = str(num)
    if str_num == str_num[::-1]:
        return True
    return False

def multiplication(k):
    new_str = "9"*k
    ai = int(new_str)
    stored_res = []
    cykle = 0
    for xi in range(ai,99,-1):
        aj = ai - cykle
        for xj in range(aj,99,-1):
            res = xi * xj
            if is_palindromic(res):
                stored_res.append(res)
        cykle = cykle + 1    
    
    return max(stored_res)
    
    
start = time.time()
product = multiplication(3)
elapsed = time.time() - start

print "The sum is %s, found in %s sec" % (product, elapsed)