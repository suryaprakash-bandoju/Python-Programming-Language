def largestElement(arr):
    # looping through array and comparing
    if len(arr) <= 1:
        return arr[0] if arr else None
    else:
        max = arr[0]
        for i in range(1,len(arr)):
            if max < arr[i]:
                max = arr[i]
        
    return max
    
    # using sort function
    # arr.sort()
    # return arr[-1]

arr = [0]
result = largestElement(arr)
print(result)