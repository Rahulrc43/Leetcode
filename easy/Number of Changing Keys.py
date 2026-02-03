class Solution :
    def countKeyChanges(self, s):
        changes = 0
        for i in range(1, len(s)):
            if s[i].lower() !=s[i - 1].lower():
                changes += 1
        return changes