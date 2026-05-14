# Find the factorial of a number

n = int(input("Enter the number: "))
if n < 0:
    print("factorial is not defined for negative numbers")
else:
    fact = 1
    for i in range(1,n+1):
        fact *= i
    print(fact)