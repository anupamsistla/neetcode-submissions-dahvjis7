from collections import deque
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        visited = set()

        def bfs(r, c):
            queue = deque()
            queue.append((r,c))
            visited.add((r,c))

            while queue:
                currR, currC = queue.popleft()

                dirs = [(0,1), (0,-1), (1, 0), (-1, 0)]

                for slackR, slackC in dirs:
                    newR, newC = currR + slackR, currC + slackC

                    if newR in range(len(grid)) and newC in range(len(grid[0])) and grid[newR][newC] == "1" and (newR, newC) not in visited:
                        visited.add((newR,newC))
                        queue.append((newR, newC))
            return

        
        numIslands = 0
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == "1" and (r,c) not in visited:
                    bfs(r,c)
                    numIslands += 1
                
        
        return numIslands

