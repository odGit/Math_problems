def is_prime(num):
    if num < 2:
        return False
    if num == 2:
        return True
    if not num & 1:
        return False
    for x in range(3, int(num**0.5)+1, 2):
        if num % x == 0:
            return False
    return True

def listing_prime(x):
    a = num_a = 0
    while a <= x:
        num_a = +1
        if is_prime(num_a):
            a=+1
    return [a, num_a]    

print listing_prime(6)