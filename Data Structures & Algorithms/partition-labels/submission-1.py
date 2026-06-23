class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        # hashmap that stores for each character the furthest index for the next same character

        furthest = {}
        
        for i in range(len(s)-1, -1, -1):
            if s[i] in furthest:
                continue
            furthest[s[i]] = i

        l,r = 0, 0
        res = []
        while r < len(s):
            maxI = furthest[s[r]]
            r = maxI

            i = 0
            while i < r:
                maxI = max(maxI, furthest[s[i]])
                r = maxI
                i += 1
            
            r = maxI
            res.append(r-l+1)
            l = r = r + 1
        return res
        


