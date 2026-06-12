class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0
        charSet = set()
        maxLen = 1

        l,r = 0, 1
        charSet.add(s[l])
        while r < len(s):
            while s[r] in charSet and l < r:
                charSet.remove(s[l])
                l += 1
            maxLen = max(r-l+1, maxLen)
            charSet.add(s[r])
            r += 1

        return maxLen