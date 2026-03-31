class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        res = set(nums)
        return len(res) != len(nums)