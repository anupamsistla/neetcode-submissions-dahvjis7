from collections import deque
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        n, m = len(grid), len(grid[0])
        visited = set()
        def bfs(i, j):
            queue = deque()

            queue.append((i, j))
            visited.add((i, j))

            dirs = [[-1, 0], [0, -1], [1, 0], [0, 1]]

            while queue:
                currI, currJ = queue.popleft()

                for stepI, stepJ in dirs:
                    newI, newJ = currI + stepI, currJ + stepJ

                    if newI in range(n) and newJ in range(m) and grid[newI][newJ] != "0" and (newI, newJ) not in visited:
                        visited.add((newI, newJ))
                        queue.append((newI, newJ))
            
            return

        count = 0
        for i in range(n):
            for j in range(m):
                if grid[i][j] == "1" and (i,j) not in visited:
                    bfs(i, j)
                    count += 1
        
        return count