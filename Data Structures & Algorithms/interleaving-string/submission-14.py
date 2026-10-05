# ax
# azyx

# axazyx 
class Solution:
    def foo(self, i, j, k, s1, s2, s3, dp):
        if dp[i][j] != -1:
            return dp[i][j]

        if i == 0 and j == 0 and k == 0:
            return True
        
        if k == 0:
            return False

        res = False
        if i > 0 and s1[i-1] == s3[k-1]:
            res |= self.foo(i-1, j, k-1, s1, s2, s3, dp)
            
        if j > 0 and s2[j-1] == s3[k-1]:
            res |= self.foo(i, j-1, k-1, s1, s2, s3, dp)
        
        dp[i][j] = res
        return dp[i][j]

    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        n, m = len(s1), len(s2)
        if (n+m) != len(s3):
            return False
        
        prev = [False] * (m+1)
    
        prev[0] = True

        for i in range(n+1):
            curr = [False] * (m+1)
            for j in range(m+1):
                if i == 0 and j == 0:
                    curr[j] = True
                    continue

                res = False
                if i > 0 and s1[i-1] == s3[i+j-1]:
                    res |= prev[j]
                    
                if j > 0 and s2[j-1] == s3[i+j-1]:
                    res |= curr[j-1]
                
                curr[j] = res
            prev = curr

        return prev[m]

