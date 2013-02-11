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
    
    
print multiplication(3)