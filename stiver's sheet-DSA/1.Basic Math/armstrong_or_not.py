n = 153

def is_armstrong(n):
    s = str(n)
    l = int(len(s))
    arm = 0
    
    for i in s:
        arm += pow(int(i),l)
    
    return arm == n

print(is_armstrong(n))