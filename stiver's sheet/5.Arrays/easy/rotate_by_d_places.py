# Brute force
# def rotateByDPlaces(arr, d):
#     n = len(arr)
#     d = d % n
#     temp = []

#     for i in range(d):
#         temp.append(arr[i])
        
#     for i in range(d, n):
#         arr[i-d] = arr[i]
        
#     for i in range(n-d, n):
#         arr[i] = temp[i-(n-d)]
        
#     return arr
    
# arr = [1,2,3,4,5,6,7]
# d = 3
# print(rotateByDPlaces(arr, d))
       

# Optimal
def rotateByD(arr, k):
    n = len(arr)
    
    if n == 0:
        return
    
    k = k%n
    
    def reverse(start, end):
        while start < end:
            arr[start], arr[end] = arr[end], arr[start]
            start += 1
            end -= 1
    
    reverse(0,n-1)
    reverse(0,k-1)
    reverse(k,n-1)
    
    return arr
    
arr = [1,2,3,4,5,6,7]
k = 3

print(rotateByD(arr, k))