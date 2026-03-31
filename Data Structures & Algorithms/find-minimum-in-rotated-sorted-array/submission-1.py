class Solution:
    def findMin(self, nums: List[int]) -> int:
        # there is a left sorted portion and a right sorted portion
        # find the min in each portion 

        l, r = 0, len(nums)-1
        minNum = float("infinity")

        while l <= r:
            mid = (l+r)//2

            minNum = min(minNum, nums[mid])

            if nums[mid] > nums[r]:
                l = mid + 1
            
            else:
                r = mid - 1
        return minNum