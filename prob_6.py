def evenly_devisible(k_max):
    sum_sqr = sum = 0
    for kx in range(1, k_max+1):
        sum_sqr = sum_sqr + kx**2
        sum = sum + kx 
    return sum**2 - sum_sqr

print evenly_devisible(100)