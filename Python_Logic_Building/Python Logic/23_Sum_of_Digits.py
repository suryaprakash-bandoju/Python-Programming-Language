# Find sum of digits of a number

n = int(input("Enter a number: "))
total = 0
if n < 0:
    n = -n
total = 0
for i in range(n):
    digit = n % 10
    total += digit
    n = n // 10
print(total)