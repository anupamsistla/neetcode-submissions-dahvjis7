class Solution:
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
        