# -*- coding: utf-8 -*-
"""
Created on Tue Oct  8 00:50:47 2013

@author: olgis


Using names.txt text file containing over 5000 first names, begin by sorting
it into alphabetical order. Then working out the alphabetical value for each
name, multiply this value by its alphabetical position in the list to obtain
a name score.

For example,
 In alphabeticaly sorder list, COLIN
 - is 3 + 15 + 12 + 9 + 14 = 53,
 - is the 938th name in the list. 
 COLIN would obtain a score of 938 × 53 = 49714.

What is the total of all the name scores in the file?

"""

import time
import string



def names_list(text_file):
    with open(text_file, "r") as f:
        output = f.read()
    
    my_list = []
    for name in output.split(","):
        name = name.replace('"', '').strip()
        my_list.append(str(name))
        
    my_list.sort()
    return my_list

def names_score(txt):
    names = names_list(txt)
    alphas = list(string.ascii_uppercase)  #building a list with aplhabet
    name_dict = {}


    for n in xrange(len(names)):
        letter_sum = 0
        for letter in names[n]:
            letter_sum += alphas.index(letter) + 1 # without + 1, A is 0

        name_dict[names[n]] = letter_sum * (n + 1) # without + 1 1st name is 0
    
    return name_dict

            

start = time.time()    
a = names_score("names.txt")
product = sum(a.values())
elapsed = time.time() - start

print "The result is %s, found in %s sec."  %(product, elapsed)
# The result is 871198282, found in 0.0321888923645 sec.

