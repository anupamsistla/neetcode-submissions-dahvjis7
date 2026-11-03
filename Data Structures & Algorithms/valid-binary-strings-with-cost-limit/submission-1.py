class Solution:
    def generateValidStrings(self, n: int, k: int) -> list[str]:
        res = []

        def dfs(i, n, k, curr):
            if k < 0:
                return
            
            if n == 0:
                res.append("".join(curr))
                return
            
            if curr and curr[-1] == "1":
                curr.append("0")
                dfs(i+1, n-1, k, curr)
                curr.pop()
            
            else:
                curr.append("0")
                dfs(i+1, n-1, k, curr)
                curr.pop()
                curr.append("1")
                dfs(i+1, n-1, k-i, curr)
                curr.pop()
            
        dfs(0, n, k, [])
        return res