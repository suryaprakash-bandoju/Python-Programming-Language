def quickSort(arr, low, high):
    if low < high:
        pivotInd = partition(arr, low, high)
        quickSort(arr, low, pivotInd - 1)
        quickSort(arr, pivotInd + 1, high)
    return arr

def partition(arr, low, high):
    pivot = arr[high]
    i = low - 1
    for j in range(low, high):
        if arr[j] <= pivot:
            i = i + 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i+1], arr[high] = arr[high], arr[i+1]
    return i + 1

arr = [4,6,2,5,7,9,1,3]
quickSort(arr, 0, len(arr)-1)
print(arr)