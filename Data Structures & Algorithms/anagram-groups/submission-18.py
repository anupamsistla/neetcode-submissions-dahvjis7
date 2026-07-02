from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashMap = defaultdict(list)

        for s in strs:
            key = [0]*26
            for c in s:
                index = ord(c)-ord("a")
                key[index] += 1
            
            hashMap[tuple(key)].append(s)
        
        return list(hashMap.values())