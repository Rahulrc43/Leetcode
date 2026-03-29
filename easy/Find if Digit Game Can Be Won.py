class Solution(object):
    def canAliceWin(self, nums):
        total_sum = sum(nums)
        sum_single = sum(x for x in nums if x < 10)
        sum_double = sum(x for x in nums if 10 <= x <= 99)
        if sum_single > total_sum - sum_single:
            return True
        if sum_double > total_sum - sum_double:
            return True
        return False
