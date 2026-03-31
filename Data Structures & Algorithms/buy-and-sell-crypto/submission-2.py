class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxProfit = 0
        minBuy = prices[0]
        profit = 0
        for price in prices:
            profit = price - minBuy
            maxProfit = max(maxProfit, profit)
            minBuy = min(minBuy, price)
        return maxProfit
