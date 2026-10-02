from collections import defaultdict
class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        outDegree = defaultdict(int)
        inDegree = defaultdict(int)

        for a, b in trust:
            outDegree[a] += 1
            inDegree[b] += 1
        
        for i in range(1, n+1):
            if inDegree[i] == n-1 and outDegree[i] == 0:
                return i
                
        return -1