class Solution:
    def foo(self, i, hashSet, s, dp):
        if i == len(s):
            return True
        
        if dp[i] != -1:
            return dp[i]

        
        currWord = ""
        res = False
        for j in range(i, len(s)):
            currWord += s[j]

            if currWord in hashSet:
                res |= self.foo(j + 1, hashSet, s, dp)
            
        dp[i] = res
        return dp[i]
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        hashSet = set(wordDict)
        n = len(s)
        
        dp = [-1] * (n + 1)
        dp[-1] = True

        for i in range(n-1, -1, -1):
            currWord = ""
            res = False
            for j in range(i, len(s)):
                currWord += s[j]

                if currWord in hashSet:
                    res |= dp[j + 1]
                
            dp[i] = res

        return dp[0]
        