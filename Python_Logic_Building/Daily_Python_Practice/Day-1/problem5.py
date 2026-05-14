# Q5.Check wheather a number us prime or not using for loop
number = int(input("Enter the numeber: "))
if number <=1:
    print("Not a Prime Number")
else:
    for i in range(2,number):
        if(number % i == 0):
            print("Not a Prime Number")
            break
    else:
        print("Prime Number")