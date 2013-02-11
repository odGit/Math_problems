def power_digit(a, p):
    sum = 0
    for letter in str(a ** p):
        sum += int(letter)
    return sum
    
    
print power_digit(2,1000)