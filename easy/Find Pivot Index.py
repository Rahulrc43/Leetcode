class Solution(object):
    def pivotIndex(self, nums):
        total = sum(nums)
        left_sum = 0
        for i, n in enumerate(nums):
            if left_sum == total - left_sum - n:
                return i
            left_sum += n
        return -1
