class Solution:
    def findMin(self, nums: List[int]) -> int:
        l,r = 0, len(nums)-1
        minNum = nums[l]

        while l <= r:
            if nums[l] < nums[r]:
                return min(nums[l], minNum)

            mid = (l+r)//2
            minNum = min(minNum, nums[mid])

            if nums[mid] >= nums[l]:
                l= mid + 1
            
            else:
                r = mid - 1

        return minNum

            
