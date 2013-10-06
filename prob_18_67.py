# -*- coding: utf-8 -*-
"""
Created on Sun Oct  6 22:40:19 2013

@author: olgis

Problem 18/67

Find the maximum total from top to bottom of the triangle.txt and triangle_small.txt

Solution:
    
    We will start from the bottom and work the way up through the triangle
    until we reach the top. Calculating  a + max(b,c), where a is level above
    the b and c.
    
"""
import time

def convert_input(txt_file):
    with open(txt_file, "r") as f:
        output = f.readlines()
    
    triangle = []
    
    for line in output:
        k = []
        for d in line.split():
            if d.isdigit():
                k.append(int(d))
                
        triangle.append(k)
               
    return triangle

def count_bottom_up(text_file):
    triangle = convert_input(text_file)
    bottom_row = len(triangle) - 1
    for x in xrange(bottom_row, 0, -1):
        upper = len(triangle[x-1])
        for y in xrange(0, upper):
            triangle[x-1][y] = triangle[x-1][y]+max(triangle[x][y],triangle[x][y+1])
        
    return triangle[0][0]
            
        




start = time.time()
product = count_bottom_up("triangle.txt")
elapsed = time.time() - start

print "The result is %s, found in %s seconds" %(product, elapsed)
#Problem 18: The result is 1074, found in 0.000264167785645 seconds
#Problem 67: The result is 7273, found in 0.00902104377747 seconds