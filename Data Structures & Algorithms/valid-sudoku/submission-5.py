class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = defaultdict(set)
        cols = defaultdict(set)

        blocks = defaultdict(set)

        for r in range(len(board)):
            for c in range(len(board[r])):
                if board[r][c] == ".":
                    continue
                if board[r][c] in rows[r]:
                    return False
                rows[r].add(board[r][c])

        
        for r in range(len(board)):
            for c in range(len(board[r])):
                if board[c][r] == ".":
                    continue
                if board[c][r] in cols[r]:
                    return False
                cols[r].add(board[c][r])
        
        for r in range(len(board)):
            for c in range(len(board[r])):
                if board[r][c] == ".":
                    continue
                if board[r][c] in blocks[(r//3, c//3)]:
                    return False
                blocks[(r//3,c//3)].add(board[r][c])
        
        return True