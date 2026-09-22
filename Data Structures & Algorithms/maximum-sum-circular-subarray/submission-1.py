class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        currMax, currMin = 0, 0
        globMax, globMin = nums[0], nums[0]
        total = 0

        for n in nums:
            currMax = max(currMax+n, n)
            currMin = min(currMin + n, n)

            globMax = max(globMax, currMax)
            globMin = min(globMin, currMin)
            total += n

        return max(globMax, total - globMin) if globMax > 0 else globMax     
        