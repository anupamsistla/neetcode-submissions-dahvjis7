from collections import deque
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        visited = set()
        def bfs(i, j):
            queue = deque()

            queue.append((i, j))
            visited.add((i,j))

            dirs = [[0,1], [1, 0], [-1, 0], [0, -1]]

            while queue:
                currI, currJ = queue.popleft()

                for stepI, stepJ in dirs:
                    newI, newJ  = currI + stepI, currJ + stepJ

                    if newI in range(len(grid)) and newJ in range(len(grid[0])) and grid[newI][newJ] == "1" and (newI, newJ) not in visited:
                        queue.append((newI, newJ))
                        visited.add((newI, newJ))
                
            return
        
        count = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if (i,j) not in visited and grid[i][j] == "1":
                    bfs(i, j)
                    count += 1
        
        return count