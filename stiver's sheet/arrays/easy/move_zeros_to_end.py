def moveZerosToEnd(arr):
    n = len(arr)
    if n == 0:
        return
    
    # Brute force
    # temp = []
    # zeros_count = 0
    
    # for num in arr:
    #     if num != 0:
    #         temp.append(num)
    #     else:
    #         zeros_count += 1
    
    # temp.extend([0] * zeros_count)
    
    # for i in range(n):
    #     arr[i] = temp[i]
    
    # optimal
    
    j = -1
    for i in range(n):
        if arr[i] == 0:
            j = i
            break
        
    if j == -1:
        return arr
    
    for i in range(j+1, n):
        if arr[i] != 0:
            arr[i], arr[j] = arr[j], arr[i]
            j += 1
    return arr


arr = [1,0,1,2,0,4,5,0,0]
print(moveZerosToEnd(arr))
