from collections import defaultdict
class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        edges = defaultdict(list)
        for u, v, w in times:
            edges[u].append((v, w))
        
        minHeap = [(0,k)]
        visited = set()
        total = 0
        while minHeap:
            w, curr = heapq.heappop(minHeap)
            if curr in visited:
                continue
            
            visited.add(curr)
            total = max(total, w)
            for nei, weight in edges[curr]:
                if not nei in visited:
                    heapq.heappush(minHeap, (w + weight, nei))
        
        return total if len(visited) == n else -1
        