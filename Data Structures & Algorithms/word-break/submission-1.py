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
        dp = [-1] * len(s)
        return self.foo(0, hashSet, s, dp)
        