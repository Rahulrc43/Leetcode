class Solution(object):
    def firstUniqueChar(self , s):
        count =  defaultdict(int)

        for c in s:
            count[c] += 1

        for i, s in enumerate(s):
            if count[c] == 1:
                return i
        return -1