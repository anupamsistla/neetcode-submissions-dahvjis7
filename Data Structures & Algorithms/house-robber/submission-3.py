class Solution:
    def foo(self, index, canRob, nums, dp):
        if dp[index][canRob] != -1:
            return dp[index][canRob]

        if index == 0:
            return nums[0] if canRob == 1 else 0
                   
        take = 0
        if canRob == 1:
            take = nums[index] + self.foo(index-1, 0, nums, dp)
        
        notTake = self.foo(index-1, 1, nums, dp)
        dp[index][canRob] = max(take, notTake)
        return dp[index][canRob]
        
    def rob(self, nums: List[int]) -> int:
        dp = [[-1]*2 for _ in range(len(nums))]
        return self.foo(len(nums)-1, 1, nums, dp)