# Q7.Input: A number,Output: Sum of all its digits

number = int(input("Enter the number: "))
sum = 0
while number > 0:
    sum += number % 10
    number = number // 10

print("Sum of digits: ",sum)