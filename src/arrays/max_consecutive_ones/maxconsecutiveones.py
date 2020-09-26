# Time O(n)

def solution_one(nums):
    count = 0
    maxCount = 0
    for num in nums:
        if(num == 1):
            count = count + 1
        else:
            count = 0
            maxCount = max(count, maxCount)
    return max(count, maxCount)


def solution_two(nums):
    maxCount = 0
    maxHere = 0
    for num in nums:
        maxHere = 0 if(num == 0) else maxHere + 1
        maxCount = max(maxCount, maxHere)
    return maxCount