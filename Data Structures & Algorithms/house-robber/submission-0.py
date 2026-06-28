class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        prev2, prev = 0, nums[0]
        
        for i in range(1, n):
            pick = nums[i] + prev2
            notPick = prev
            prev2 = prev
            prev = max(pick, notPick)
        
        return prev
