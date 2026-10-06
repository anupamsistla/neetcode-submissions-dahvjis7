class Solution:
    def foo(self, i, s, dp):
        if i == len(s):
            return 1
        
        if dp[i] != -1:
            return dp[i]

        numWays = 0
        
        if s[i] != "0":
            numWays += self.foo(i+1, s, dp)
            
            if i + 2 <= len(s) and s[i:i+2] <= "26":
                numWays += self.foo(i+2, s, dp)
    
        dp[i] = numWays

        return numWays
            
    def numDecodings(self, s: str) -> int:
        dp = [-1]*len(s)
        return self.foo(0, s, dp)
        