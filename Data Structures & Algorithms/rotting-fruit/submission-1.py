from collections import deque
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        # we go level by level essentially

        queue = deque()

        m = len(grid)
        n = len(grid[0])
        
        fresh = 0

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    fresh += 1
                if grid[i][j] == 2:
                    queue.append((i,j))
        
        directions = [[0,1], [0, -1], [1, 0], [-1, 0]]
        time = 0
        while queue and fresh > 0:
            for i in range(len(queue)):
                r, c = queue.popleft()

                for slackR, slackC in directions:
                    newR = r + slackR
                    newC = c + slackC

                    if newR in range(m) and newC in range(n) and grid[newR][newC] == 1:
                        grid[newR][newC] = 2
                        queue.append((newR, newC)) 
                        fresh -= 1

            time += 1

        return time if fresh == 0 else -1
            



                

    