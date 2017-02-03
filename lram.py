def lram(n):
    pi=3.141592653589793
    lower = 4
    upper = 8    
    delta = (upper - lower)* 1.0/n
    i = lower
    result = 0
    while i < upper:
        result = result + pi*(64 - i**2)*delta
#        print result
        i = i + delta
    return result
