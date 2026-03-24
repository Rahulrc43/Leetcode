class Solution(object):
    def romanToInt(self, s):
        vals = {'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
        total = 0
        prev = 0
        for c in reversed(s):
            v = vals[c]
            total = total - v if v < prev else total + v
            prev = v
        return total
