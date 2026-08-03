from collections import defaultdict
class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        count = defaultdict(int)
    
        for n in nums:
            count[n] += 1
        
        i = 0
        j = 0
        while i < len(nums):
            while count[j] == 0:
                j += 1
            nums[i] = j
            count[j] -= 1
            i += 1
            
        return
