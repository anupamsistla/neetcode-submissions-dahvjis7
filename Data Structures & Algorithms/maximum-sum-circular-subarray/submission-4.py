class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        currSum = 0
        currMinSum = 0
        globMax = nums[0]
        globMin = nums[0]
        total = 0

        for n in nums:
            currSum = max(currSum + n, n)
            currMinSum = min(currMinSum + n, n)
            globMax = max(globMax, currSum)
            globMin = min(globMin, currMinSum)
            total += n

        return max(globMax, total - globMin) if globMax > 0 else globMax