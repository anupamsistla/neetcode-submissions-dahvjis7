class Solution:
    def foo(self, i, j, k, s1, s2, s3, dp):
        if i < 0 and j < 0 and k < 0:
            return True
        
        if k < 0:
            return False
        
        if dp[i][j] != -1:
            return dp[i][j]

        if i >= 0 and s1[i] == s3[k]:
            dp[i][j] = self.foo(i-1, j, k-1, s1, s2, s3, dp)
            return dp[i][j]
        
        if j >= 0 and s2[j] == s3[k]:
            dp[i][j] = self.foo(i, j-1, k-1, s1, s2, s3, dp)
            return dp[i][j]

        dp[i][j] = False
        return dp[i][j]

    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        n = len(s1)
        m = len(s2)
        k = len(s3)
        dp = [[-1]*(m+1) for _ in range(n+1)]
        return self.foo(n-1, m-1, k-1, s1, s2, s3, dp)

        