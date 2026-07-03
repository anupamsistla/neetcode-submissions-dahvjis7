class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        res = len(nums)

        for i in range(len(nums)):
            res = res ^ nums[i]
            res = res ^ i
        
        return res