class Solution:
    def findMin(self, nums: List[int]) -> int:
        l,r = 0, len(nums)-1
        minNum = float("inf")
        while l <= r:
            mid = (l+r)//2

            if nums[l] <= nums[mid]:
                minNum = min(minNum, nums[l])
                l = mid + 1

            elif nums[mid] <= nums[r]:
                minNum = min(minNum, nums[mid])
                r = mid - 1
        return minNum
        
            
            

            