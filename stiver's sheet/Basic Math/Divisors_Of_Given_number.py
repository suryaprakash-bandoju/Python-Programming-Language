import math

n = 36

def divisors_of_given_number(n):
    div = []
    for i in range(1, n+1):
        if n % i == 0:
            div.append(i)
    
    return div

print(divisors_of_given_number(n))


def optimal_solution(n):
    div = []
    
    for i in range(1, math.isqrt(n) + 1):
        
        if n % i == 0:
            div.append(i)
            
            if i != n // i:
                div.append(n // i)
                
    return div

print(optimal_solution(n))