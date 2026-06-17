class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        seen = set()
        N = len(board)
        M = len(board[0])
        index = 0

        def dfs(index, i, j):
            if index == len(word):
                return True
            if i not in range(N) or j not in range(M) or word[index] != board[i][j] or (i, j) in seen:
                return False
            
            seen.add((i,j))
            res = dfs(index+1, i+1, j) or dfs(index+1, i-1, j) or dfs(index+1, i, j+1) or dfs(index+1, i, j-1)
            seen.remove((i,j))
            return res
        
        for i in range(N):
            for j in range(M):
                if dfs(0, i, j):
                    return True
        
        return False

        

            