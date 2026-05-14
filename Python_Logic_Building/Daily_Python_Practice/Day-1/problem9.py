# Q9.Check wheather a number is a polindrome

number = int(input("Enter the number: "))
original = number
digit = 0
reverse = 0
while number > 0:
    digit = number % 10
    reverse = reverse * 10 + digit
    number = number // 10

if original == reverse:
    print("Polindrome")
else:
    print("Not a Polindrome")
