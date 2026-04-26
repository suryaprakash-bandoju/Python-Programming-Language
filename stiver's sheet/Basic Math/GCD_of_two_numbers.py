n1 = 9
n2 = 12

def gcd_is(n1, n2):
    fact1 = []
    fact2 = []
    for i in range(1, n1+1):
        if n1 % i == 0:
            fact1.append(i)
    for j in range(1, n2+1):
        if n2 % j == 0:
            fact2.append(j)
    
    gcd = list(set(fact1) & set(fact2))
    return max(gcd)

print(gcd_is(n1, n2))

def better(n1, n2):
    
    while n2:
        n1, n2 = n2, n1 % n2
    return n1
    
print(better(n1, n2))