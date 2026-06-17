class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        
        mapping = {
            2: ["a", "b", "c"], 
            3: ["d", "e", "f"],
            4: ["g", "h", "i"],
            5: ["j", "k", "l"],
            6: ["m", "n", "o"],
            7: ["p", "q", "r", "s"],
            8: ["t", "u", "v"],
            9: ["w", "x", "y", "z"]
        }

        self.res = []

        def dfs(subset, i):
            if i == len(digits):
                self.res.append("".join(subset))
                return
            
            for c in mapping[int(digits[i])]:
                subset.append(c)
                dfs(subset, i+1)
                subset.pop()
        
        dfs([], 0)
        return self.res
