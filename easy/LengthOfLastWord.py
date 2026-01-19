class Solution:
    def lengthOfLastWord(self, s):
        words = s.split()
        if words:
            return len(words[-1])
        return 0
  