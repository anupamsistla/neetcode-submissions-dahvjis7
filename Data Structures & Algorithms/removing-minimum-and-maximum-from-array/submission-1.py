class Solution:
    def minimumDeletions(self, nums: list[int]) -> int:
        maxI, minI = 0, 0 
        maxElem, minElem = float("-inf"), float("inf")

        for i, n in enumerate(nums):
            if n > maxElem:
                maxElem = n
                maxI = i
        
            if n < minElem:
                minElem = n
                minI = i

        
        leftSide = min(maxI, minI)
        rightSide = max(maxI, minI)
        
        return min(leftSide + 1 + min(rightSide - leftSide, len(nums) - rightSide), len(nums) - rightSide + min(rightSide - leftSide, leftSide + 1))
