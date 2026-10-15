class Solution:
    def foo(self, i, j, s, p, m, n, dp):
        if (i, j) in dp:
            return dp[(i, j)]

        if j == n:
            return i == m
        
        match = i < m and (s[i] == p[j] or p[j] == ".")
    
        if j + 1 < n and p[j+1] == "*":
            dp[(i,j)] = self.foo(i, j+2, s, p, m, n, dp) or (match and self.foo(i+1, j, s, p, m, n, dp))
            return dp[(i, j)]
        
        if match:
            dp[(i, j)] = self.foo(i+1, j+1, s, p, m, n, dp)
            return dp[(i, j)]
        
        dp[(i, j)] = False
        return dp[(i, j)]
        
    def isMatch(self, s: str, p: str) -> bool:
        dp = {}
        return self.foo(0,0, s, p, len(s), len(p), dp)

        