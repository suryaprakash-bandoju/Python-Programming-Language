# Input two numbers. Print all even numbers between them

n1 = int(input("Enter the number: "))
n2 = int(input("Enter the number: "))
for i in range(n1,n2+1):
    if i % 2 != 0:
        print(i)