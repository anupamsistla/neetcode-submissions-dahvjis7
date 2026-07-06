from collections import defaultdict
import heapq
class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        edges = defaultdict(list)

        for u, v, w in times:
            edges[u].append((v, w))
        
        visited = set()

        minHeap = [(0, k)]

        maxCost = 0

        while minHeap:
            currW, currU = heapq.heappop(minHeap)

            if currU in visited:
                continue
            
            visited.add(currU)
            
            maxCost = max(maxCost, currW)

            for nextV, nextW in edges[currU]:
                if nextV in visited:
                    continue
                
                heapq.heappush(minHeap, (currW + nextW, nextV))
        
        print(len(visited))
        return maxCost if len(visited) == n else -1