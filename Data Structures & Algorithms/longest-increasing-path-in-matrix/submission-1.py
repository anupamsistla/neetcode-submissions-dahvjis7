class Solution:
    def foo(self, i, j, prev, matrix, dp):
        if i < 0 or j < 0 or i >= len(matrix) or j >= len(matrix[0]) or matrix[i][j] <= prev:
            return 0
        
        if dp[i][j] != -1:
            return dp[i][j]

        up = 1 + self.foo(i-1, j, matrix[i][j], matrix, dp)
        down = 1 + self.foo(i+1, j, matrix[i][j], matrix, dp)
        left = 1 + self.foo(i, j-1, matrix[i][j], matrix, dp)
        right = 1 + self.foo(i, j+1, matrix[i][j], matrix, dp)
    
        dp[i][j] = max(up, down, left, right)
        return dp[i][j]

    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        n, m = len(matrix), len(matrix[0])
        maxRes = 0
        dp = [[-1] * m for _ in range(n)]

        for i in range(n):
            for j in range(m):
                maxRes = max(maxRes, self.foo(i, j, -1, matrix, dp))
        
        return maxRes