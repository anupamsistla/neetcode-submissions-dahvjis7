class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l,r = 0, 0
        currWindow = set()
        maxLen = 0
        while r < len(s):
            while s[r] in currWindow:
                currWindow.remove(s[l])
                l +=1 
            
            currWindow.add(s[r])
            maxLen = max(maxLen, r - l + 1)
            r += 1
            
        return maxLen
