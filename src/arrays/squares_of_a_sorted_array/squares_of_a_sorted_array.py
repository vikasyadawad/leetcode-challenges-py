def solution_one(nums):
    result = [0] * len(nums)
    left_index = 0
    right_index = len(nums) - 1
    while left_index <= right_index:
        left = abs(nums[left_index])
        right = abs(nums[right_index])
        if left > right:
            result[right_index - left_index] = left * left
            left_index += 1
        else:
            result[right_index - left_index] = right * right
            right_index -= 1
    return result
