class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        currMax, currMin = 1, 1
        res = max(nums)

        for n in nums:
            temp = currMax
            currMax = max(currMax * n, currMin * n, n)
            currMin = min(temp * n , currMin * n, n)
            res = max(res, currMax)
        
        return res