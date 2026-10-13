class Solution:
    def foo(self, target, nums, dp):
        if dp[target] != -1:
            return dp[target]

        if target == 0:
            return 1
        
        res = 0
        for i in range(len(nums)):
            if nums[i] <= target:
                res += self.foo(target-nums[i], nums, dp)
            
        dp[target] = res
        return dp[target]

    def combinationSum4(self, nums: List[int], target: int) -> int:
        dp = [-1] * (target+1)
        dp[0] = 1

        for target in range(1, target + 1):
            res = 0
            for i in range(len(nums)):
                if nums[i] <= target:
                    res += dp[target-nums[i]]
                
            dp[target] = res

        return dp[target]