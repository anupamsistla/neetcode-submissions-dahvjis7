class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxProfit = 0
        profit = 0
        minBuy = prices[0]

        for i in range(1, len(prices)):
            profit = prices[i] - minBuy
            maxProfit = max(maxProfit, profit)
            minBuy = min(minBuy, prices[i])

        if maxProfit < 0:
            return 0
        return maxProfit
