from collections import deque
class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        m = len(grid)
        n = len(grid[0])
        queue = deque()
        visited = set()

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 0:
                    queue.append((i, j))
                    visited.add((i, j))

        dist = 0
        dirs = [[0,1], [0,-1], [1, 0], [-1, 0]]

        while queue:
            for i in range(len(queue)):
                currI, currJ = queue.popleft()
                grid[currI][currJ] = dist

                for stepI, stepJ in dirs:
                    newI, newJ = currI + stepI, currJ + stepJ

                    if newI in range(m) and newJ in range(n) and grid[newI][newJ] != -1 and (newI, newJ) not in visited:
                        visited.add((newI, newJ))
                        queue.append((newI, newJ))
            dist += 1
    
        return

                





