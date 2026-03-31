from collections import deque
class Solution:
    
    def numIslands(self, grid: List[List[str]]) -> int:
        numIslands = 0
        visited = set()
        def bfs(r, c):
            queue = deque()

            queue.append((r, c))
            visited.add((r,c))
            
            dirs = [[1, 0], [-1, 0], [0, 1], [0, -1]]
            while queue:
                oldR, oldC = queue.popleft()
                for dirR, dirC in dirs:
                    newR, newC = dirR + oldR, dirC + oldC
                    if newR < len(grid) and newR >= 0 and newC < len(grid[0]) and newC >= 0 and grid[newR][newC] == "1" and (newR, newC) not in visited:
                        queue.append((newR, newC))
                        visited.add((newR, newC))
            return
                
        
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == "1" and (r,c) not in visited:
                    bfs(r,c)
                    numIslands += 1

        
        return numIslands
        