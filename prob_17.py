# -*- coding: utf-8 -*-
"""
Created on Sat Oct  5 13:27:12 2013

@author: olgis

Number letter count

If the numbers 1 to 5 are written out in words: one, two, three, four, five,
 then there are 3 + 3 + 5 + 4 + 4 = 19 letters used in total.

PROBLEM:
 If all the numbers from 1 to 1000 (one thousand) inclusive were written out 
 in words, how many letters would be used?

NOTE: Do not count spaces or hyphens.
For example, 342 (three hundred and forty-two) contains 23 letters and
 115 (one hundred and fifteen) contains 20 letters.
 The use of "and" when writing out numbers is in compliance with British usage.

"""

import time

num_to_let_dict = {0:"", 1:"one", 2: "two", 3: "three", 4: "four",
                    5: "five", 6: "six", 7: "seven", 8: "eight", 9: "nine",
                    10: "ten", 11: "eleven",12: "twelve", 13: "thirteen",
                    14: "fourteen", 15: "fifteen", 16: "sixteen", 17: "seventeen",
                    18: "eighteen", 19: "nineteen", 20: "twenty", 30: "thirty",
                    40: "forty", 50: "fifty",  60: "sixty",  70: "seventy",
                    80: "eighty", 90: "ninety", 100: "hundred",1000: "thousand"}
                
def num_to_let(start, end, my_dict):
    res = 0
    for i in xrange(start, end + 1):
        #checking how many 1000 in a number
        n = i // 1000 
        if n > 0:
            res += (len(my_dict[n]) + len(my_dict[1000]))
            i -= n*1000
        #checking how many 100 in number    
        k = i // 100 
        if k > 0:
            res += (len(my_dict[k]) + len(my_dict[100]))
            p = i % 100
            i -= k*100
            if p > 0: res += 3 #for AND in "one hundred and fifteen"
        
            
        if i < 21:
            res += len(my_dict[i])
        else: 
            f = i % 10
            l = i - f
            res += (len(my_dict[l]))
            if f > 0:
                res += (len(my_dict[f]))

    return res
        
start = time.time()
product = num_to_let(1, 1000, num_to_let_dict)
elapsed = time.time() - start

print "The result is %s, found in %s sec" %(product, elapsed)
#The result is 21124, found in 0.00138807296753 sec