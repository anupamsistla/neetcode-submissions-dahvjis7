class Solution:
    def findMin(self, nums: List[int]) -> int:
        l,r = 0, len(nums)-1
        minElem = float("inf")

        while l <= r:
            mid = (l+r)//2

            if nums[l] <= nums[mid]:
                minElem = min(minElem, nums[l])
                l = mid + 1

            else:
                minElem = min(minElem, nums[mid])
                r = mid - 1
        
        return minElem
