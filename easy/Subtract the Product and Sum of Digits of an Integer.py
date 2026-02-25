class Solution(object):
    def subtractProductAndSum(self, n):
        product = 1
        total_sum = 0
        for digit in str(n):
            d = int(digit)
            product *= d
            total_sum += d
        return product - total_sum
