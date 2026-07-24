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
        prev = [0]*2
        
        # base case:
        prev[1] = nums[0]

        for index in range(1, len(nums)):
            curr = [0]*2
            for canRob in range(2):
                take = 0
                if canRob == 1:
                    take = nums[index] + prev[0]
                
                notTake = prev[1]
                curr[canRob] = max(take, notTake)
            prev = curr

        return prev[1]