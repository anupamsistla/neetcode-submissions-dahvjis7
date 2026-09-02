class Solution:
    def numSubseq(self, nums: List[int], target: int) -> int:
        nums.sort()
        l,r = 0, len(nums)-1
        res = 0
        while l <= r:
            currSum = nums[l] + nums[r]

            if currSum <= target:
                res += 2 ** (r-l+1) - 2 ** (r-l)
                l += 1
            else:
                r -= 1
        
        return res % (10**9+7)
