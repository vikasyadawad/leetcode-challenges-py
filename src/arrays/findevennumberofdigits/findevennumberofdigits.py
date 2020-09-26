def solution_one(nums):
    return sum(len(str(n)) % 2 == 0 for n in nums)