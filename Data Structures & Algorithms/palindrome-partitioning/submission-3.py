class Solution:
    def isPali(self, s):
        l,r = 0, len(s) - 1
        while l < r:
            if s[l] == s[r]:
                l += 1
                r-=1
            else:
                return False
        return True

    def partition(self, s: str) -> List[List[str]]:
        res = []
        def dfs(subset, i):
            if i == len(s):
                res.append(subset.copy())
                return
            
            for j in range(i+1, len(s)+1):
                curr = s[i:j]
                if self.isPali(curr):
                    subset.append(curr)
                    dfs(subset, j)
                    subset.pop()
        dfs([], 0)
        return res


        

        