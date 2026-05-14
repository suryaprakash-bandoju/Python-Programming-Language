n = int(input())
# i = int(input())
# def printNum(i, n):
#     if i == n+1:
#         return
#     print(i)
#     printNum(i+1, n)

# printNum(n, i)


def printNto1(n):
    if n < 1:
        return
    print(n)
    printNto1(n-1)
    
printNto1(n)