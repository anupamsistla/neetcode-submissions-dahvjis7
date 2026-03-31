class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        map1 = dict()
        map2 = dict()

        for c in s:
            map1[c] = 0

        for c in s:
            map1[c] += 1

        for c in t:
            map2[c] = 0
        
        for c in t:
            map2[c] += 1
        
        return map1 == map2
    
        