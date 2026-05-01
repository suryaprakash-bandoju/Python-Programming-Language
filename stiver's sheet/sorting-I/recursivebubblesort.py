def recursiveBubbleSort(arr, n):
    if n == 1:
        return arr
    
    swapped = False
    for i in range(n-1):
        if arr[i] > arr[i+1]:
            arr[i], arr[i+1] = arr[i+1], arr[i]
            swapped = True
    if not swapped:
        return arr
    return recursiveBubbleSort(arr, n-1)
    
arr = [13, 46, 24, 52, 20, 9]

result =recursiveBubbleSort(arr, len(arr))
print(result)