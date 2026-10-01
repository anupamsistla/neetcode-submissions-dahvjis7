from collections import deque
class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        q = deque()
        visited = set()
        startI, startJ = 0, 0

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    startI, startJ = i, j

        q.append((startI, startJ))
        visited.add((startI, startJ))
        perimeter = 0
        
        neighbors = [[-1, 0], [1, 0], [0, 1], [0, -1]]

        while q:
            currI, currJ = q.popleft()

            for stepI, stepJ in neighbors:
                newI, newJ = currI + stepI, currJ + stepJ

                if newI in range(len(grid)) and newJ in range(len(grid[0])) and grid[newI][newJ] == 1:
                    if (newI, newJ) not in visited:
                        q.append((newI, newJ))
                        visited.add((newI, newJ))
                    
                else:
                    perimeter += 1
        
        return perimeter
            