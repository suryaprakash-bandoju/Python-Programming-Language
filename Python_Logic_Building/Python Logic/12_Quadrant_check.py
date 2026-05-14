# Check if a point (x,y) is in first, second, third and fourth quardrant

x = float(input("Enter the x value: "))
y = float(input("Enter the y value: "))
if x > 0 and y > 0:
    print("First Quadrant")
elif x < 0 and y > 0:
    print("Second Quadeant")
elif x < 0 and y < 0:
    print("Third Quadrant")
elif x > 0 and y < 0:
    print("Fourth Quadrant")
else:
    print("The point is on axis")