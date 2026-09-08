class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        i = 0


        while i < len(nums):
            target = -nums[i]
            l,r = i+1, len(nums)-1

            while l < r:
                currSum = nums[l] + nums[r]

                if currSum == target:
                    res.append([nums[i], nums[l], nums[r]])
                    l += 1

                    while r > l and nums[r] == nums[r-1]:
                        r -= 1
                    
                    r -= 1
                
                elif currSum < target:
                    l += 1
                
                else:
                    r -= 1
                

            i += 1
            while i < len(nums) and nums[i] == nums[i-1]:
                i += 1
            
        return res
                    
                
            


