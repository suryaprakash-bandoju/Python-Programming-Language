# Check if a triangle is valid

print("Triangle validity cheker")
print("Enter the lengths of three sides:")
side1 = float(input("Enter the 1st side: "))
side2 = float(input("Enter the 2nd side: "))
side3 = float(input("Enter the 3rd side: "))

if side1 <= 0 or side2 <= 0 or side3 <= 0:
    print("Invalid triangle: All side must be Positive")
else:
    if (side1 + side2 > side3) and (side1 + side3 > side2) and (side2 + side3 > side1):
        print("These side can form a valid triangle")
    else:
        print("These side cannot form a valid triangle")