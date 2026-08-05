class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        res = []

        i = 0

        while i < len(nums):
            j = i + 1

            while j < len(nums):
                l,r = j + 1, len(nums)-1

                toFind = target - nums[i] - nums[j]

                while l < r:
                    currSum = nums[l] + nums[r]

                    if currSum == toFind:
                        res.append([nums[i], nums[j], nums[l], nums[r]])
                    
                        l += 1

                        while r > l and nums[r] == nums[r-1]:
                            r -= 1
                        
                        r -= 1
                    
                    elif currSum < toFind:
                        l += 1
                    
                    else:
                        r -= 1

                while j < len(nums)-1 and nums[j] == nums[j + 1]:
                    j += 1
                
                j += 1

            while i < len(nums)-1 and nums[i] == nums[i + 1]:
                i += 1
            
            i += 1
        
        return res
                    
        