class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s2) < len(s1):
            return False
        count1 = [0]*26
        count2 = [0]*26

        for c in s1:
            count1[ord(c)-ord("a")] += 1
        
        l,r = 0, 0
        while r < len(s2):
            if r-l+1 > len(s1):
                count2[ord(s2[l])-ord("a")]-=1
                l +=1 
            
            count2[ord(s2[r])-ord("a")] += 1
            if count1 == count2:
                return True
            
            r += 1
        return False
