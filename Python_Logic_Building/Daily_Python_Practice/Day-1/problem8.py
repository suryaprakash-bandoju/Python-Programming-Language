# Q8.Reverse the digit of a number using loop

number = int(input("Enter the number: "))
reverse = 0
digit = 0
while number > 0:
    digit = number % 10
    reverse = reverse * 10 + digit
    number = number // 10
print("Reversed number:",reverse)