'''
Grade calculator:
A:90+
B:80-89
C:70-79
D:60-69
F:<60
'''

marks = float(input("Enter your marks: "))
if marks < 0 or marks > 100:
    print("Invalid marks: Please enter the marks between 0 to 100")
else:
    if marks >= 90:
        print("A")
    elif marks >= 80:
        print("B")
    elif marks >= 70:
        print("C")
    elif marks >= 60:
        print("D")
    else:
        print("F")