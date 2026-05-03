def secondSmallest(arr):
    largest = arr[0]
    ssmallest = float("inf")

    for i in range(1, len(arr)):
        if arr[i] < largest:
            ssmallest = largest
            largest = arr[i]

        if arr[i] < ssmallest and arr[i] != largest:
            ssmallest = arr[i]

    print(ssmallest)


arr = [1, 2, 4, 7, 7, 5]
secondSmallest(arr)
