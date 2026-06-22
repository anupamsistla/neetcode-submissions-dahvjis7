class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxSum = nums[0]
        currSum = nums[0]

        l,r = 0, 1

        while r < len(nums):
            if currSum < 0:
                currSum = 0
                l = r 
            
            currSum += nums[r]
            print(currSum)
            maxSum = max(currSum, maxSum)
            r += 1
    
        return maxSum
