class Solution(object):
    def triangleType(self, nums):
        a, b, c = nums
        if a + b <= c or a + c <= b or b + c <= a:
            return "none"
        if a == b == c:
            return "equilateral"
        if a == b or b == c or a == c:
            return "isosceles"
        return "scalene"
