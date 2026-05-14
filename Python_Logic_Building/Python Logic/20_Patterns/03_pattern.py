'''
A
A B
A B C
A B C D
'''

n = int(input("Enter the number of rows: "))
alphabets = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
for i in range(0, n):
    for j in range(0, i + 1):
        print(alphabets[j], end="")
    print()
