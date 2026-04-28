arr = [1,2,1,3,4,5]

def frequencyCount(arr):
    seen = {}

    for i in arr:
        if i in seen:
            seen[i] += 1
        else:
            seen[i] = 1

    return max(seen)

result = frequencyCount(arr)

for num,count in result.items():
    print(num, count)
