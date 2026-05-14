def duplicats(arr):
    seen = set()
    
    for num in arr:
        if num not in seen:
            seen.add([arr[num]])
            
    return seen

arr = [1,1,2,2,2,3,3]

print(duplicats(arr))