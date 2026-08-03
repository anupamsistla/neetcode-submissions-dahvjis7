class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        n, m = len(matrix), len(matrix[0])
        self.dp = [[0] * (m+1) for _ in range(n+1)]

        for r in range(n):
            prefix = 0
            for c in range(m):
                prefix += matrix[r][c]
                above = self.dp[r][c+1]
                self.dp[r + 1][c + 1] = prefix + above
        return

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        r1, c1, r2, c2 = row1 + 1, col1 + 1, row2 + 1, col2 + 1
        bottomRight = self.dp[r2][c2]
        left = self.dp[r2][c1-1]
        topLeft = self.dp[r1-1][c1 - 1]
        above = self.dp[r1-1][c2]
        
        return bottomRight - left - above + topLeft
        

# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)