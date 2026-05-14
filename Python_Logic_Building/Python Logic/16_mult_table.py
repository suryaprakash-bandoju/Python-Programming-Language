# Print multiplication table of a given number


n = int(input("Enter the number: "))
for i in range(1,11):
    print(f"{n} X {i} = {n*i}")


n = int(input("Enter the number: "))
i = 1
while i <= 10:
    print(f"{n} X {i} = {n*i}")
    i += 1
