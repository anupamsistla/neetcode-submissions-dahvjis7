class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        candidates.sort()
        def dfs(subset, i, currSum):
            if currSum == target:
                res.append(subset.copy())
                return
            
            if i == len(candidates) or currSum > target:
                return
            
            subset.append(candidates[i])
            dfs(subset, i+1, currSum + candidates[i])
            subset.pop()

            while i + 1 < len(candidates) and candidates[i] == candidates[i+1]:
                i += 1
            
            dfs(subset, i+1, currSum)
        dfs([], 0, 0)
        return res