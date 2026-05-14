s = "madam"
i = 0

def isPalindrome(s, i):
    n = len(s)
    
    if i >= n//2:
        return True
    if s[i] != s[n-i-1]:
        return False
    return isPalindrome(s, i+1)

res = isPalindrome(s, i)
print(res)
