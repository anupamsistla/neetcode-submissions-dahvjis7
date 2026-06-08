from collections import deque, defaultdict
class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        adjList = defaultdict(list)
        inDegree = defaultdict(int)

        for u,v in edges:
            adjList[u].append(v)
            adjList[v].append(u)
            inDegree[u] += 1
            inDegree[v] += 1
        
        queue = deque()
        N = len(edges)

        for i in range(1, N+1):
            if inDegree[i] == 1:
                queue.append(i)

        while queue:
            curr = queue.popleft()

            for nei in adjList[curr]:
                inDegree[nei] -=1
                
                if inDegree[nei] == 1:
                    queue.append(nei)
        
        for u, v in reversed(edges):
            if inDegree[u] == 2 and inDegree[v] == 2:
                return [u,v]
        return []
                
        
