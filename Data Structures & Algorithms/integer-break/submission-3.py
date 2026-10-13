class Solution:
    
    def integerBreak(self, n: int) -> int:
        dp = [-1] * (n+1)

        def foo(num, dp):
            if dp[num] != -1:
                return dp[num]

            if num == 1:
                return 1
            
            maxRes = 0 if n == num else num
            for i in range(1, num):
                maxRes = max(maxRes, i * foo(num-i, dp))
            
            dp[num] = maxRes
            return dp[num]

        return foo(n, dp)
        