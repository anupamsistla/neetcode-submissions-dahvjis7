class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        def dfs(subset, numOpen, numClose):
            if numOpen == numClose == n:
                res.append("".join(subset))
                return
            
            if numOpen < n:
                subset.append("(")
                dfs(subset, numOpen+1, numClose)
                subset.pop()
            
            if numClose < numOpen:
                subset.append(")")
                dfs(subset, numOpen, numClose+1)
                subset.pop()
                
        dfs([], 0, 0)
        return res