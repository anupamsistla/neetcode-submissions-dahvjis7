class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        currSet = set()

        hashMap = {}

        for c in s:
            hashMap[c] = 1 + hashMap.get(c, 0)

        currLen = 0
        res = []
        for c in s:
            hashMap[c] -= 1
            currSet.add(c)
            currLen += 1

            if hashMap[c] == 0:
                currSet.remove(c)

            if len(currSet) == 0:
                res.append(currLen)
                currLen = 0
        
        return res

        