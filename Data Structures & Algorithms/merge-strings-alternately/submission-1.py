class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        l = 0

        r = len(word1) if len(word1) <= len(word2) else len(word2)
        res = ""
        while l < r:
            res += word1[l]
            res += word2[l]
            l+=1
        
        res += word1[l:]
        res+= word2[l:]
        return res
