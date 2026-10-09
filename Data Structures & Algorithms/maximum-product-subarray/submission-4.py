class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        currMax, currMin = 1, 1
        res = max(nums)

        for n in nums:
            temp = currMax
            currMax = max(n * currMax, n * currMin, n)
            currMin = min(n * temp, n * currMin, n)
            res = max(res, currMax)
        
        return res