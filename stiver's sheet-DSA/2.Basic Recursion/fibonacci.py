n = 5


# def printFibonacci(n):
#     if n==0:
#         print("0")
#     elif n==1:
#         print("0 1")
    
#     else:
#         fib = [0] * (n+1)
#         fib[0]=0
#         fib[1]=1
        
#         for i in range(2, n+1):
#             fib[i] = fib[i-1] + fib[i-2]
            
#         print(" ".join(str(num) for num in fib))
        
# printFibonacci(n)



def Recursive(n):
    if n<=1:
        return n
    
    last = Recursive(n-1)
    slast = Recursive(n-2)
    return last + slast

print(Recursive(n))