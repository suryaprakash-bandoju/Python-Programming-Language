def findMissingNumber(arr):
    n = len(arr) + 1
    # Brute Force
    # for i in range(1, n):
    #     found = False
    #     for j in range(n - 1):
    #         if arr[j] == i:
    #             found = True
    #             break
    #     if not found:
    #         return i
    # return -1

    #------------------------------------------------------
    # Optimal
    
    totalSum = sum(arr)
    
    expSum = n * (n + 1) // 2
    
    return expSum - totalSum

arr = [8,4,5,3,2,1,7]

result = findMissingNumber(arr)
print(result)