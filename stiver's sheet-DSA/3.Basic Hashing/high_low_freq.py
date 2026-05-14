arr = [10,5,10,15,10,5]
def max_min_freq(arr):
    freq = {}
    for num in arr:
        freq[num] = freq.get(num, 0)+1
        
    max_freq = -1
    max_element = None
    min_freq = float('inf')
    min_element = None

    for num, count in freq.items():
        if count>max_freq:
            max_freq = count
            max_element = num
            
        if count < min_freq:
            min_freq = count
            min_element = num
    return max_element, min_element

highest, lowest = max_min_freq(arr)
print(highest, lowest)