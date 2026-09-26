class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        searchSpace = []

        for t in triplets:
            if t[0] > target[0] or t[1] > target[1] or t[2] > target[2]:
                continue
            
            searchSpace.append(t)
        
        if not searchSpace:
            return False

        maxA, maxB, maxC = searchSpace[0][0], searchSpace[0][1], searchSpace[0][2]
        
        for t in searchSpace:
            maxA = max(maxA, t[0])
            maxB = max(maxB, t[1])
            maxC = max(maxC, t[2])
    
        return [maxA, maxB, maxC] == target