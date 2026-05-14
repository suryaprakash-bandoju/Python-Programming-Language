# Find the largest of 3 numbers

n1 = int(input("Enter the 1st number: "))
n2 = int(input("Enter the 2nd number: "))
n3 = int(input("Enter the 3rd number: "))

if n1 == n2 == n3:
    print("Three numbers are equel")
else:
    if n1 > n2 and n1 > n3:
        print(f"{n1} is larger")
    elif n2 > n1 and n2 > n3:
        print(f"{n2} is larger")
    elif n3 > n1 and n3 > n2:
        print(f"{n3} is larger")