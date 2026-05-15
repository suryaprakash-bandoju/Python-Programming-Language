def length_of_longest_subArray(arr, n):

    mpp: dict[int, int] = {}
    maxi = 0
    s = 0

    for i in range(n):
        s += arr[i]

        if s == 0:
            maxi = i + 1
        else:
            if s in mpp:
                maxi = max(maxi, i - mpp[s])
            else:
                mpp[s] = i
        return maxi

arr = [9, -3, 3, -1, 6, -5]
n = len(arr)
print(length_of_longest_subArray(arr,n))
