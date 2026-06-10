from collections import defaultdict
import heapq
class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        edges = defaultdict(list)
        
        for u, v, w in times:
            edges[u].append((v,w))
        
        minHeap = [(0,k)]
        visited = set()
        t = 0

        while minHeap:
            w1, u1 = heapq.heappop(minHeap)
            if(u1 in visited):
                continue
            
            visited.add(u1)
            t = max(t, w1)

            for v2, w2 in edges[u1]:
                if v2 not in visited:
                    heapq.heappush(minHeap, (w1+w2, v2))
        
        return t if len(visited) == n else -1