def linearSearch(arr, num):
    
    # for i in range(len(arr)):
    #     if num == arr[i]:
    #         return i
        
    # return -1
    
    if num in arr:
        return arr.index(num)
    return -1

arr = [1, 2, 3, 4, 5]
num = 6
print(linearSearch(arr, num))