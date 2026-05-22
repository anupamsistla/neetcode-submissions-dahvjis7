class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        currMin = float("inf")
        maxProfit = float("-inf")

        for p in prices:
            currMin = min(currMin, p)
            
            maxProfit = max(maxProfit, p - currMin)
        
        return maxProfit if not maxProfit == float("-inf") else 0
