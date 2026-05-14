# Q3.Swap two numbers using arithmetic operation(no temp variable).
n1 = int(input("Enter the number: "))
n2 = int(input("Enter the number: "))

n1 = n1+n2
n2 = n1-n2
n1 = n1-n2
print("After Swaping:")
print("n1 = ",n1)
print("n2 = ",n2)