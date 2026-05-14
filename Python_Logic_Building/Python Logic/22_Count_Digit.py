# Count digit in a number

n = 0
count = 0
if n == 0:
    count = 0
else:
    if n < 0:
        n = -n
    count = 0
    while n > 0:
        n = n // 10
        count += 1
print(count)