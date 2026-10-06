class Solution:
    def foo(self, i, s, encodeMap, dp):
        if i == len(s):
            return 1
        
        if dp[i] != -1:
            return dp[i]
        
        numWays = 0
        currKey = ""
        for j in range(i, len(s)):
            currKey += s[j]

            if currKey in encodeMap:
                numWays = numWays + self.foo(j+1, s, encodeMap, dp)
            
        dp[i] = numWays     
        return dp[i]
            
    def numDecodings(self, s: str) -> int:
        encodeMap = set(["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13", "14", "15", "16", "17", "18", "19", "20", "21", "22", "23", "24", "25", "26"])
        dp = [-1] * len(s)
        return self.foo(0, s, encodeMap, dp)
    
        