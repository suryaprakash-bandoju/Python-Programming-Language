# Count vowels and consonants in a string
str = input("Enter a string: ")
vowels = 0
cons = 0
for i in range(len(str)):
    if("a" or "e" or "i" or "o" or "u" == str[i]):
        vowels += 1
    else:
        cons += 1
print(f"Vowels: {vowels}, Consonants: {cons}")