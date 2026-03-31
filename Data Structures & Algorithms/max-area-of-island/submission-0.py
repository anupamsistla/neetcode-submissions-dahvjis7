from collections import deque
class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        visited = set()

        def bfs(r,c):
            queue = deque()

            queue.append((r,c))
            visited.add((r,c))

            res = 0
            while queue:
                currR, currC = queue.popleft()
                res += 1
                dirs = [(0,1), (0,-1), (1, 0), (-1, 0)]
                
                for dirR, dirC in dirs:
                    newR, newC = currR + dirR, currC + dirC

                    if newR in range(len(grid)) and newC in range(len(grid[0])) and grid[newR][newC] == 1 and (newR, newC) not in visited:
                        visited.add((newR, newC))
                        queue.append((newR, newC))
            
            return res
 
        maxArea = 0
        
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == 1 and (r,c) not in visited:
                    currMax = bfs(r,c) 
                    maxArea = max(maxArea, currMax)

        return maxArea            