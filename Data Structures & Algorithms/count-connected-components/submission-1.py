from collections import defaultdict, deque
class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        if not edges:
            return 0

        adjList = defaultdict(list)
        queue = deque()

        for a, b in edges:
            adjList[b].append(a)
            adjList[a].append(b)


        visited = set()

        def dfs(ver):
            if ver in visited:
                return

            visited.add(ver)
            for nei in adjList[ver]:
                dfs(nei)
        
        count = 0
        for i in range(n):
            if i not in visited:
                count += 1
                dfs(i)

        return count
                
        

        