def appearOnce(arr):
    # Brute force
    # for i in range(len(arr)):
    #     num = arr[i]
    #     count = 0
    #     for j in range(len(arr)):
    #         if arr[j] == num:
    #             count += 1
    #     if count == 1:
    #         return num
    
    #Optimal XOR-Method
    
    xor = 0
    for i in range(len(arr)):
        xor = xor^arr[i]
    return xor

arr = [2,2,1,1,3,4,4]
print(appearOnce(arr))
