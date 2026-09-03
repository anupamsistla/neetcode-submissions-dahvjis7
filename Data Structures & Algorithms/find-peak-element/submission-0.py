class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        l,r = 0, len(nums)-1

        while l <= r:
            mid = (l+r)//2

            leftMid = mid - 1
            if leftMid in range(len(nums)):
                leftMid = nums[leftMid]
            else:
                leftMid = float("-inf")
            
            rightMid = mid + 1
            if rightMid in range(len(nums)):
                rightMid = nums[rightMid]
            else:
                rightMid = float("-inf")
            
            if leftMid < nums[mid] and rightMid < nums[mid]:
                return mid
            
            if leftMid > nums[mid]:
                r = mid - 1
            
            else:
                l = mid + 1
        
        return -1