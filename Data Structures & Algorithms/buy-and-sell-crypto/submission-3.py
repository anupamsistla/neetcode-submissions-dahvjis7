class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        currMin = float("inf")
        currMax = float("-inf")
        for price in prices:
            currMin = min(currMin, price)

            currMax = max(currMax, price - currMin)
        
        return currMax