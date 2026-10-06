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

        return numWays
            
    def numDecodings(self, s: str) -> int:
        encodeMap = set(["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13", "14", "15", "16", "17", "18", "19", "20", "21", "22", "23", "24", "25", "26"])
        dp = [0] * (len(s)+1)
        dp[len(s)] = 1

        for i in range(len(s)-1, -1, -1):
            numWays = 0
            currKey = ""
            for j in range(i, len(s)):
                currKey += s[j]
                
                if currKey in encodeMap:
                    numWays = numWays + dp[j+1]
            
            dp[i] = numWays
            
        return dp[0]
    
        