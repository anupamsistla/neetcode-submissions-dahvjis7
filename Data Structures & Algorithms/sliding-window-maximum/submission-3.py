class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        res = list()
        l = 0
        for r in range(len(nums)):
           
            if r-l+1 == k:
                i = l
                currMax = float("-infinity")
                while i < r + 1 and r < len(nums):
                    currMax = max(currMax, nums[i])
                    i +=1
                res.append(currMax)
                l += 1
        
        return res