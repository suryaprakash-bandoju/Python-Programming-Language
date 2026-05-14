def unionOfTwoSortedArrays(arr1, arr2):
    j = 0
    i = 0
    result = []
    m = len(arr1)
    n = len(arr2)

    while i < m and j < n:
        if arr1[i] < arr2[j]:
            if not result or result[-1] != arr1[i]:
                result.append(arr1[i])
            i += 1
        elif arr1[i] > arr2[j]:
            if not result or result[-1] != arr2[j]:
                result.append(arr2[j])
            j += 1
        else:
            if not result or result[-1] != arr1[i]:
                result.append(arr1[i])
            i += 1
            j += 1

    while i < m:
        while i < m - 1 and arr1[i] == arr1[i+1]:
            i+=1
        result.append(arr1[i])
        i+=1
    while j < n:
        while j < n -1 and arr2[j] == arr2[j+1]:
            j += 1
        result.append(arr2[j])
        j += 1

    return result


arr1 = [1,1,2,3,4,5]
arr2 = [2,3,4,4,5,6]

print(unionOfTwoSortedArrays(arr1, arr2))
