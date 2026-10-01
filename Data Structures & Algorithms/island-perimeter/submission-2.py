from collections import deque
class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        q = deque()
        neighbors = [[0,1], [0, -1], [1, 0], [-1, 0]]

        startI, startJ = 0, 0

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    startI, startJ = i, j
    
        q.append((startI, startJ))
        perimeter = 0
        visited = set()

        visited.add((startI, startJ))

        while q:
            startI, startJ = q.popleft()

            for stepI, stepJ in neighbors:
                newI, newJ = startI + stepI, startJ + stepJ
                
                if newI in range(len(grid)) and newJ in range(len(grid[0])) and grid[newI][newJ] == 1:
                    if (newI, newJ) not in visited:
                        q.append((newI, newJ))
                        visited.add((newI, newJ))
                
                else:
                    perimeter += 1
        return perimeter
                
            