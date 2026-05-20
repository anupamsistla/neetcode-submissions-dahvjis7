class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = defaultdict(list)

        for s in strs:
            iden = [0] * 26
            
            for c in s:
                iden[ord(c)-ord("a")] += 1
            
            
            groups[tuple(iden)].append(s)
        
        return list(groups.values())
