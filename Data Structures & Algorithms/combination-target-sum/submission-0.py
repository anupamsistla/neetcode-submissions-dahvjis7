class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        
        curr = []
        res = []
        def dfs(i, total):
            if total == target:
                res.append(curr.copy())
                return

            if i >= len(nums) or total > target:
                return
            
            curr.append(nums[i])
            dfs(i, total + nums[i])

            curr.pop()
            dfs(i+1, total)
        
        dfs(0, 0)
        return res