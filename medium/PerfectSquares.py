class Solution(object):
    def numSquares(self, n):
        dp = [float('inf')] * (n + 1)
        dp[0] = 0
        squares = []
        i = 1
        while i * i <= n:
            squares.append(i * i)
            i += 1
        for i in range(1, n + 1):
            for sq in squares:
                if sq > i:
                    break
                dp[i] = min(dp[i], dp[i - sq] + 1)
        return dp[n]
