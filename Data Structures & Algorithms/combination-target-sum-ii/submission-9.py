class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        candidates.sort()
        
        def dfs(subset, i, currSum):
            if currSum == target:
                res.append(list(subset))
                return
            
            if i == len(candidates) or currSum > target:
                return

            # Include the current candidate
            subset.append(candidates[i])
            dfs(subset, i+1, currSum + candidates[i])
            subset.pop()
            
            # Skip duplicate candidates to avoid redundant branches
            while i + 1 < len(candidates) and candidates[i] == candidates[i+1]:
                i += 1
            dfs(subset, i+1, currSum)
        
        dfs([], 0, 0)

        return res