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
        dp = [[0]*2 for _ in range(len(nums))]
        
        # base case:
        dp[0][1] = nums[0]

        for index in range(1, len(nums)):
            for canRob in range(2):
                take = 0
                if canRob == 1:
                    take = nums[index] + dp[index-1][0]
                
                notTake = dp[index-1][1]
                dp[index][canRob] = max(take, notTake)

        return dp[len(nums)-1][1]