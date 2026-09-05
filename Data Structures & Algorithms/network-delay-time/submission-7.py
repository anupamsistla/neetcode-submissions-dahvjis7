from collections import defaultdict 
import heapq
class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        visited = set()
        adjList = defaultdict(list)

        for u, v, w in times:
            adjList[u].append((v, w))
            
        
        res = 0
        pq = [(0, k)]

        while pq:
            wI, curr = heapq.heappop(pq)
            if curr in visited:
                continue
            
            res = max(res, wI)
            visited.add(curr)

            for nei, w in adjList[curr]:
                heapq.heappush(pq, (wI + w, nei))
        
        return res if len(visited) == n else -1