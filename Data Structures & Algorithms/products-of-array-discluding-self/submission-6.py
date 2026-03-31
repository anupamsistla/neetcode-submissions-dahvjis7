class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        leftProd = [1]*len(nums)
        
        left = 1
        for i in range(len(nums)):
            leftProd[i] = left
            left *=nums[i]

        rightProd = [1]*len(nums)
        right = 1
        for i in range(len(nums)-1, -1, -1):
            rightProd[i] = right
            right *= nums[i]
        
        res = [1]*len(nums)
        for i in range(len(nums)):
            res[i] = leftProd[i]*rightProd[i]
        
        return res