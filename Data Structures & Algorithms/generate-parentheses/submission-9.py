class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []

        def dfs(subset, openC, closedC):
            if openC == closedC == n:
                res.append("".join(subset))
                return
            
            if openC < n:
                subset.append("(")
                dfs(subset, openC+1, closedC)
                subset.pop()
            
            if closedC < openC:
                subset.append(")")
                dfs(subset, openC, closedC+1)
                subset.pop()
        
        dfs([], 0, 0)
        return res