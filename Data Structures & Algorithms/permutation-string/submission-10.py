class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        l = 0
        freq1 = [0]*26
        freq2 = [0]*26

        for c in s1:
            index = ord(c)-ord("a")
            freq1[index] += 1

        for r in range(len(s2)):
            if(r-l+1 > len(s1)):
                index = ord(s2[l]) - ord("a")
                freq2[index] -=1
                l += 1
            
            index = ord(s2[r]) - ord("a")
            freq2[index] +=1
        
            if(freq1 == freq2):
                return True

        return False