def twoSum(nums, target):
    seen = {}
    for i, num in enumerate(nums):
        compliment = target - num
        
        if compliment in seen:
            return [seen[compliment], i]
        
        seen[num] = i
    return []

nums = [1,2,3,5,6,8,11]
target = 14

result = twoSum(nums, target)
print(result)