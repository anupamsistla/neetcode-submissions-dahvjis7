class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []

        def dfs(subset, i, currSum):
            if currSum == target:
                res.append(subset.copy())
                return 
            
            if i == len(nums) or currSum > target:
                return
            
            currSum += nums[i]
            subset.append(nums[i])
            dfs(subset, i, currSum)
            
            currSum -= nums[i]
            subset.pop()
            dfs(subset, i+1, currSum)

        dfs([], 0, 0)
        return res