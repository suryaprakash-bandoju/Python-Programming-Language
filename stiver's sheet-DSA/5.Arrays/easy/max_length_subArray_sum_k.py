def maxLengthSumSubArrayK(nums,k):
    n = len(nums)
    maxLen = 0
    left = 0
    right = 0
    sum = nums[0]
    while right < n:
        while left <= right and sum > k:
            sum -= nums[left]
            left += 1
        if sum == k:
            maxLen = max(maxLen, right - left + 1)
        right += 1
        if right < n:
            sum += nums[right]
    return maxLen

nums = [1,2,3,5,6,4,3,1,1,1]
k = 3
result = maxLengthSumSubArrayK(nums, k)
print(result)