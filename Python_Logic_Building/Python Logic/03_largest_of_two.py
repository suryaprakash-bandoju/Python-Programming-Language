# Find the largest of two numbers

n1 = int(input("Enter 1st number: "))
n2 = int(input("Enter 2nd number: "))
if n1 == n2:
    print("Equel")
elif n1 > n2:
    print(f"{n1} is large")
elif n1 < n2:
    print(f"{n2} is large")
