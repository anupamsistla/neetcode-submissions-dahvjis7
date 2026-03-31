class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        
        curr = []

        res = set()


        def dfs(i, currSum):
            if currSum == target:
                res.add(tuple(curr.copy()))
                return
                
            if i == len(candidates) or currSum > target:
                return
            
            
            curr.append(candidates[i])
            dfs(i+1, currSum + candidates[i])

            curr.pop()
            dfs(i+1, currSum)
        
        candidates.sort()
        dfs(0, 0)

        return [list(s) for s in res]
