class Solution:
    def isPalindrome(self, s):
        filtered_s = ''.join(char.lower() for char in s if char.isalnum())
        return filtered_s == filtered_s[::-1]
