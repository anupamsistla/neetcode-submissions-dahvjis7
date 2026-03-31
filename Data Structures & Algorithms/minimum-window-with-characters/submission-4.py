class Solution:
    def minWindow(self, s: str, t: str) -> str:
        # current approach, thinking of having two maps
        if t == "":
            return ""
        countT, window = {}, {}

        for c in t:
            countT[c] = 1 + countT.get(c, 0)

        l = 0
        have, need = 0, len(countT)
        res, maxLen = [-1, -1], float("infinity")
        for r in range(len(s)):
            window[s[r]] = 1 + window.get(s[r], 0)

            if s[r] in countT and window[s[r]] == countT[s[r]]:
                have += 1

            while have == need:
                if(r-l+1 < maxLen):
                    maxLen = r-l+1
                    res = [l,r]

                window[s[l]] -=1
                if s[l] in countT and window[s[l]] < countT[s[l]]:
                    have -= 1
                l+=1
        
        l,r = res
        if maxLen != float("infinity"):
            return s[l:r+1]
        else:
            return ""

                    
     