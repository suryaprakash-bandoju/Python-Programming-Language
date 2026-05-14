# Check if a character is vowel or consonant

char = input("Enter a Character: ").lower()
if len(char) != 1:
    print("Please enter a single character.")
else:
    if char in 'aeiou':
        print(f"{char} is a Vowel.")
    elif char.isalpha():
        print(f"{char} is a consonant.")
    else:
        print(f"{char} is not a letter.")
            