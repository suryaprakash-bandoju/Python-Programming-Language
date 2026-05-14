def removeDuplicates(arr):
    n = len(arr)
    if n == 0:
        return 0
    j = 0
    for i in range(1, n):
        if arr[i] != arr[j]:
            j += 1
            arr[j] = arr[i]
    
    return j+1

arr = [1,1,2,2,2,3,3]

print(removeDuplicates(arr))
     