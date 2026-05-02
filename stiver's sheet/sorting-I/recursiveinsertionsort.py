def InsertionSort(arr, i, n):
    if i == n:
        return
    j = i
    while j > 0 and arr[j - 1] > arr[j]:
        arr[j-1], arr[j] =  arr[j], arr[j-1]
        j -= 1
    InsertionSort(arr, i+1, n)
    
    

arr = [13, 46, 24, 52, 20, 9]
InsertionSort(arr, 0, len(arr))
print(arr)