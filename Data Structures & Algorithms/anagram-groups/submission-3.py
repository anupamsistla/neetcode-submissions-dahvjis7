class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = defaultdict(list)

        for s in strs:
            currKey = "".join(sorted(s))
            groups[currKey].append(s)

        return list(groups.values())
