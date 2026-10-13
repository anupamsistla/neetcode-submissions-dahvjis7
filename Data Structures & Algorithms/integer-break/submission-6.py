class Solution:
    def integerBreak(self, n: int) -> int:
        dp = [-1] * (n+1)
        dp[1] = 1

        for num in range(2, n+1):
            maxRes = 0 if num == n else num

            for i in range(1, num):
                maxRes = max(maxRes, i * dp[num - i])

            dp[num] = maxRes

        return dp[n]      