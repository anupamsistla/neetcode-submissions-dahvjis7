from collections import deque
class Solution:
    def solve(self, board: List[List[str]]) -> None:
        ROWS = len(board)
        COLS = len(board[0])

        def dfs(i,j):
            if i not in range(ROWS) or j not in range(COLS) or board[i][j] != "O":
                return
            
            board[i][j] = "T"
            dfs(i-1, j)
            dfs(i+1, j)
            dfs(i, j-1)
            dfs(i, j+1)

        for i in range(ROWS):
            for j in range(COLS):
                if i in [0, ROWS-1] or j in [0, COLS-1] and board[i][j] == "O":
                    dfs(i,j)
        
        for i in range(ROWS):
            for j in range(COLS):
                if board[i][j] == "O":
                    board[i][j] = "X"
        
        for i in range(ROWS):
            for j in range(COLS):
                if board[i][j] == "T":
                    board[i][j] = "O"
        