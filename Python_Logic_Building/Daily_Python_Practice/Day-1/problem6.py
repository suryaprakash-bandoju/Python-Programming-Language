# Q6.Print the multiplication table of any number from to 10
number = int(input("Enter the number from 1 to 10: "))
for i in range (1,11):
    print(f"{number} X {i} = {number * i}")