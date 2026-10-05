class Solution:
    def foo(self, i, j, k, s1, s2, s3, dp):
        if i == 0 and j == 0 and k == 0:
            return True
        
        if k == 0:
            return False
        
        if i > 0 and s1[i-1] == s3[k-1]:
            dp[i][j] = self.foo(i-1, j, k-1, s1, s2, s3, dp)
            return dp[i][j]
        
        if j > 0 and s2[j-1] == s3[k-1]:
            dp[i][j] = self.foo(i, j-1, k-1, s1, s2, s3, dp)
            return dp[i][j]
        
        dp[i][j] = False
        return dp[i][j]

    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        n, m = len(s1), len(s2)

        if (n + m) != len(s3):
            return False
        
        prev = [False]*(m+1)

        prev[0] = True

        for i in range(n+1):
            curr = [False]*(m+1)
            for j in range(m+1):
                if i == 0 and j == 0:
                    curr[j] = True
                    continue

                if i > 0 and s1[i-1] == s3[i+j-1] and prev[j]:
                    curr[j] = prev[j]
                
                if j > 0 and s2[j-1] == s3[i+j-1] and curr[j-1]:
                    curr[j] = curr[j-1]
            
            prev = curr
        return prev[m]

