class Solution(object):
    def twoSum(self, nums, target):
        r = {}
        for i, num in enumerate(nums):
            t = target - num
            if t in r:
                return [r[t], i]
            r[num] = i
        return [] 