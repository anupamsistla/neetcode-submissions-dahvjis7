class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        maxSum = nums[0]
        minSum = nums[0]
        currSum = 0
        currMinSum = 0
        total = 0

        for n in nums:
            currSum = max(currSum + n, n)
            currMinSum = min(currMinSum + n, n)
            
            maxSum = max(maxSum, currSum)
            minSum = min(minSum, currMinSum)
            total += n

        print(minSum)
        return max(maxSum, total - minSum) if maxSum > 0 else maxSum