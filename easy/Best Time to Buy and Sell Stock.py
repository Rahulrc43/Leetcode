class Solution(object):
    def maxProfit(self, prices):
        min_price, max_profit = float('inf'), 0
        for p in prices:
            min_price = min(min_price, p)
            max_profit = max(max_profit, p - min_price)
        return max_profit
