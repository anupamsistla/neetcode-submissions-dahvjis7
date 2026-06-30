class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        l,r = 0, 0
        currSum, maxSum = 0, nums[0]

        
        while r < len(nums):
            currSum += nums[r]
            maxSum = max(currSum, maxSum)

            r += 1
            if currSum < 0:
                currSum = 0
                l = r
        
        return maxSum