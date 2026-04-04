from collections import deque
class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        queue = deque()
        visited = set()
        m, n = len(grid), len(grid[0])
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 0:
                    queue.append((i,j))
                    visited.add((i,j))

        dirs = [[0,1], [0, -1], [1, 0], [-1, 0]]
        dist = 0
        while queue:
            for i in range(len(queue)):
                r, c = queue.popleft()
                grid[r][c] = dist

                for dirR, dirC in dirs:
                    newR, newC = r + dirR, c + dirC

                    if newR in range(m) and newC in range(n) and (newR, newC) not in visited and grid[newR][newC] != -1:
                        queue.append((newR, newC))
                        visited.add((newR, newC))
            
            dist += 1
        

        return