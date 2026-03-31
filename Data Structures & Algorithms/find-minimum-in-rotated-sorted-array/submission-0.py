class Solution:
    def findMin(self, nums: List[int]) -> int:
        l,r = 0, len(nums)-1
        small = nums[l]
        while(l<=r):
            mid = (l+r)//2
            if(nums[l] <= nums[mid]): #left sorted portion
                small = min(small, nums[l])
                l = mid + 1

            else:
                small = min(small, nums[mid])
                r = mid - 1
        return small
