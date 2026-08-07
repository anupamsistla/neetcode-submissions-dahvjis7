class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0
        currWindow = set()
        l,r = 0, 1
        currWindow.add(s[l])
        maxLen = 1

        while l < r and r < len(s):
            while s[r] in currWindow:
                currWindow.remove(s[l])
                l +=1 
            
            currWindow.add(s[r])
            maxLen = max(maxLen, r - l + 1)
            r += 1
            
        return maxLen
