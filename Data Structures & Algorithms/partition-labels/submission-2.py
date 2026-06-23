class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        # hashmap that stores for each character the furthest index for the next same character
        furthest = {}

        for i, v in enumerate(s):
            furthest[v] = i
        
        size = end = 0

        res = []
        for i, v in enumerate(s):
            size += 1
            end = max(end, furthest[s[i]])

            if i == end:
                res.append(size)
                size = end = 0
        
        return res
        



