
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        check1 = [0]*26
        check2 = [0]*26

        for c in s:
            check1[ord(c)-ord('a')] +=1
        
        for c in t:
            check2[ord(c)-ord("a")] += 1
        
        return check1 == check2
        