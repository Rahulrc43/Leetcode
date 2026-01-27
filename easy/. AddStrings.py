class Solution:
    def addString(self,num1,num2):
        i, j = len(num1) - 1, len(num2) - 1
        carry = 0
        result = []

        while i >= 0 or j >= 0 or carry:
            digit1 = int(num1[i]) if i >= 0 else 0
            digit2 = int(num2[j]) if j >= 0 else 0

            carry, digit = divmod(d1 + d2 + carry, 10)
            res.append(str(digit))
            i -= 1
            j -= 1

        return ''.join(reversed(result))