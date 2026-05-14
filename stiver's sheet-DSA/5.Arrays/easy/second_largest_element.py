def secondLargest(arr):
    largest = arr[0]
    slargest = float('inf')
    
    for i in range(1, len(arr)):
        if arr[i] > largest:
            slargest = largest
            largest = arr[i]
            
        if arr[i] > slargest and arr[i] != largest:
            slargest = arr[i]
            
    print(slargest)
    
    
arr = [1, 2, 4, 7, 7, 5]
secondLargest(arr)