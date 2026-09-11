class Solution:
    def foo(self, i, s, words, dp):
        if i == len(s):
            return 0
        
        if dp[i] != -1:
            return dp[i]
        
        res = 1 + self.foo(i+1, s, words, dp)

        for j in range(len(s)):
            if s[i:j+1] in words:
                res = min(res, self.foo(j+1, s, words, dp))
        
        dp[i] = res
        return res

    def minExtraChar(self, s: str, dictionary: List[str]) -> int:
        words = set(dictionary)
        dp = [-1]*len(s)

        return self.foo(0, s, words, dp)