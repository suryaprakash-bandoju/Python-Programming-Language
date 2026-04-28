s = "abcabehf"

def freq_char(s):
    seen = {}
    for char in s:
        if char in seen:
            seen [char] += 1
        else:
            seen[char] = 1
    return seen

result = freq_char(s)
for char, count in result.items():
    print(char, count)