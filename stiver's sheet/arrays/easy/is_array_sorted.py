def isSorted(arr, n):
    for i in range(1, n):
            if arr[i-1] >= arr[i]:
                return False
    return True
        
arr = [1, 2, 3, 4, 5]
n = len(arr)

print(isSorted(arr, n))