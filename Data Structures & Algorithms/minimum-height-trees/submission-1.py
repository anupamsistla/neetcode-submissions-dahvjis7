from collections import defaultdict, deque
class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        adjList = defaultdict(list)

        for n1, n2 in edges:
            adjList[n1].append(n2)
            adjList[n2].append(n1)

        edge_count = {}
        leaves = deque()

        for v, neighbors in adjList.items():
            if len(neighbors) == 1:
                leaves.append(v)
            edge_count[v] = len(neighbors)
        
        while leaves:
            if n <= 2:
                return list(leaves)
            for i in range(len(leaves)):
                curr = leaves.popleft()
                n -= 1
                
                for nei in adjList[curr]:
                    edge_count[nei] -= 1

                    if edge_count[nei] == 1:
                        leaves.append(nei)
        
        return [0]
                    
                