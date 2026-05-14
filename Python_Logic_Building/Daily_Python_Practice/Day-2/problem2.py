# Reverse the digit of a number using while loop
n = int(input("Enter the number: "))
reverse = 0
digit = 0
while n > 0:
    digit = n % 10
    reverse = reverse * 10 + digit
    n = n // 10
print(reverse)