from collections import defaultdict, deque
class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if not edges:
            return True
        visited = set()

        adjList = defaultdict(list)

        for a, b in edges:
            adjList[b].append(a)
            adjList[a].append(b)

        queue = deque()
        vers = list(adjList.keys())
        queue.append((vers[0], None))
        visited.add(vers[0])

        count = 0

        while queue:
            currNode, prevNode = queue.popleft()
            count += 1
            for nei in adjList[currNode]:
                if nei == prevNode:
                    continue
                
                if nei in visited:
                    return False
                
                queue.append((nei, currNode))

        return True if count == n else  False
        

        
