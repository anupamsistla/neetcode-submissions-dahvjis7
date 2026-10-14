class Solution:
    def foo(self, i, j, prev, matrix, n, m, dp):
        if i < 0 or j < 0 or i == n or j == m or matrix[i][j] <= prev:
            return 0
        
        if dp[i][j] != -1:
            return dp[i][j]

        up = 1 + self.foo(i-1, j, matrix[i][j], matrix, n, m, dp)
        down = 1 + self.foo(i+1, j, matrix[i][j], matrix, n, m, dp)
        left = 1 + self.foo(i, j-1, matrix[i][j], matrix, n, m, dp)
        right = 1 + self.foo(i, j+1, matrix[i][j], matrix, n, m, dp)

        dp[i][j] = max(up, down, left, right)
        return dp[i][j]

    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        n = len(matrix)
        m = len(matrix[0])
        dp = [[-1] * m for _ in range(n)]
        maxRes = 0
        
        for i in range(n):
            for j in range(m):
                maxRes = max(maxRes, self.foo(i, j, -1, matrix, n, m, dp))
        
        return maxRes

        