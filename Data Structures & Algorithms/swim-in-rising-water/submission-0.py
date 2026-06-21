class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        N = len(grid)
        visited = set()
        
        minHeap = [(grid[0][0], 0, 0)]
        visited.add((0,0))

        dirs = [[0, -1], [0,1], [1,0], [-1,0]]

        while minHeap:
            t, r, c = heapq.heappop(minHeap)

            if r == N-1 and c == N-1:
                return t
            
            for dirR, dirC in dirs:
                newR, newC = r + dirR, c + dirC
                if newR in range(N) and newC in range(N) and (newR, newC) not in visited:
                    heapq.heappush(minHeap, (max(t, grid[newR][newC]), newR, newC))
                    visited.add((newR, newC))
    