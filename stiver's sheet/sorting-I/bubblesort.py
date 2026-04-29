def bubbleSort(arr):
    n = len(arr)
    
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                
    return arr

arr = [2,4,2,5,2,56,7,25]

sorted_arr = bubbleSort(arr)
print(sorted_arr)