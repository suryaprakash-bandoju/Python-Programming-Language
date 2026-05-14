# Simple Calculator

num1 = float(input("Enter the First number: "))
num2 = float(input("Enter the Second number: "))
ope = input("Enter the Operation (+,-,/,*): ")
if ope == '+':
    print(f"The Addition of {num1} and {num2} is {num1 + num2}")
elif ope == '-':
    print(f"The Subtraction of {num1} and {num2} is {num1 - num2}")
elif ope == '*':
    print(f"The Multiplication of {num1} and {num2} is {num1 * num2}")
elif ope == '/':
    if num2 != 0:
        print(f"The Division of {num1} and {num2} is {num1 / num2}")
    else:
        print("Error: Division by zero is not allowed")
else:
    print("Invalid operation")
