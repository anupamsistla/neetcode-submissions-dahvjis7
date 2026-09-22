class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        ROWS = defaultdict(set)
        COLS = defaultdict(set)
        SQUARES = defaultdict(set)


        for r in range(9):
            for c in range(9):
                if board[r][c] == ".":
                    continue
                
                if board[r][c] in ROWS[r]:
                    return False
                
                ROWS[r].add(board[r][c])
    
        for r in range(9):
            for c in range(9):
                if board[c][r] == ".":
                    continue
                
                if board[c][r] in COLS[r]:
                    return False
                
                COLS[r].add(board[c][r])
        
        for r in range(9):
            for c in range(9):
                if board[r][c] == ".":
                    continue
                
                if board[r][c] in SQUARES[(r//3, c//3)]:
                    return False
                
                SQUARES[(r//3, c//3)].add(board[r][c])
        
        return True