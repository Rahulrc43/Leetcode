class Solution:
    def sumOfMultiples(self , n):
        res = 0
        for i in range(1 , n + 1):
            if any(i % x == 0 for x in [3,5,7]):
                res += i
        return res