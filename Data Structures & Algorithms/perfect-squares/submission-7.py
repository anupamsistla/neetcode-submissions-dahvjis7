import math
class Solution:
    def foo(self, n, dp):
        if dp[n] != -1:
            return dp[n]

        if n == 0:
            return 0

        minRes = float("inf")
        for candis in range(1, n+1):
            if candis ** 2 <= n:
                minRes = min(minRes, 1 + self.foo(n-candis**2, dp))
        
        dp[n] = minRes
        return dp[n]
            
    def numSquares(self, n: int) -> int:
        dp = [-1] * (n+1)
        dp[0] = 0

        for n in range(1, n+1):
            minRes = float("inf")
            for candis in range(1, n+1):
                if candis ** 2 <= n:
                    minRes = min(minRes, 1 + dp[n-candis**2])
                else:
                    break
            
            dp[n] = minRes
        return dp[n]
    