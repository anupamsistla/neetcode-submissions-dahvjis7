class Solution:
    def maxAscendingSum(self, nums: List[int]) -> int:
        prev = 0
        maxSum = float("-inf")
        currSum = 0

        for num in nums:
            if num <= prev:
                currSum = num
            else:
                currSum += num
                
            prev = num
            maxSum = max(maxSum, currSum)
        
        return maxSum