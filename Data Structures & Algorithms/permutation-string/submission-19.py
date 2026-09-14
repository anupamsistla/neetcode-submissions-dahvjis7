class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1Map = [0]*26

        for c in s1:
            s1Map[ord(c) - ord("a")] += 1
        
        l,r = 0,0
        s2Map = [0]*26
        
        while r < len(s2):
            s2Map[ord(s2[r]) - ord("a")] += 1

            if s2Map == s1Map:
                return True
            
            if r-l+1 == len(s1):
                s2Map[ord(s2[l])-ord("a")] -= 1
                l += 1
            
            r += 1
        
        return False