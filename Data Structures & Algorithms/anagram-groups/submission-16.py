class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)

        for s in strs:
            check = [0]*26

            for c in s:
                check[ord(c)-ord('a')] += 1
            
            res[tuple(check)].append(s)

        return list(res.values())
        