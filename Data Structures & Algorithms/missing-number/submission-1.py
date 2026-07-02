class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        # our range is 0 -> n = len(nums)
        # each element in nums is in this range and there are no duplicates
        # length of nums is n
        sumRange = len(nums)

        for i in range(len(nums)):
            sumRange += i
            sumRange -= nums[i]
       
        return sumRange

