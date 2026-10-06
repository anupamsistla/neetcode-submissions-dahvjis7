class Solution:
    def numDecodings(self, s: str) -> int:
        next1, next2 = 1, 0
        
        for i in range(len(s)-1, -1, -1):
            numWays = 0
        
            if s[i] != "0":
                numWays += next1
                
                if i + 2 <= len(s) and s[i:i+2] <= "26":
                    numWays += next2
        
            next2 = next1
            next1 = numWays

        return next1
        