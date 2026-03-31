from collections import deque
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        visited = set()
        numIslands = 0

        def bfs(r, c):
            queue = deque()
            visited.add((r,c))
            queue.append((r, c))
        
            dirs = [[1,0], [-1,0], [0, 1], [0, -1]]

            while queue:
                oldR, oldC = queue.popleft()
                
                for dirR, dirC in dirs:
                    newR, newC = oldR + dirR, oldC + dirC

                    if newR in range(len(grid)) and newC in range(len(grid[0])) and grid[newR][newC] == "1" and (newR, newC) not in visited:
                        visited.add((newR, newC))
                        queue.append((newR, newC))
            return


        
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == "1" and (r,c) not in visited:
                    bfs(r, c)
                    numIslands += 1
        
        return numIslands