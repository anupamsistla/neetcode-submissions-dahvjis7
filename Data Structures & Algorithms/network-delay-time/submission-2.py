from collections import defaultdict
import heapq
class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        edges = defaultdict(list)
        visited = set()

        for u, v, w in times:
            edges[u].append((v,w))
        
        t = 0

        minHeap = [(0,k)]

        while minHeap:
            w1, u1 = heapq.heappop(minHeap)

            if u1 in visited:
                continue
            
            visited.add(u1)
            t = max(w1, t)

            for v1, w2 in edges[u1]:
                if v1 not in visited:
                    heapq.heappush(minHeap, (w1+w2, v1))
        
        return t if len(visited) == n else -1