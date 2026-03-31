class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = set()
        curr = []
        def dfs(i):
            if i >= len(nums):
                res.add(tuple(curr.copy()))
                return
            
            curr.append(nums[i])
            dfs(i+1)

            curr.pop()
            dfs(i+1)
        
        nums.sort()
        dfs(0)
        return [list(s) for s in res]