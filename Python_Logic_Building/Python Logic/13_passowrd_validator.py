# simple password validator

password = input("Enter your password: ")
length_ok = len(password) >= 8
has_digit = any(char.isdigit() for char in password)
if length_ok and has_digit:
    print("Valid password")
else:
    print("Invalid password")
