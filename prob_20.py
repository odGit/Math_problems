import time

def factor(n):
    res = 1
    for n in range(1,n+1):
        res *= n
    return res

def frac_dig_sum(num):
    prod = 0
    for dig in str(num):
        prod += int(dig)
    return prod

print frac_dig_sum(factor(100))