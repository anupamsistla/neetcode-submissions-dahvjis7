class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l,r = 0, len(heights)-1
        currArea = float("-inf")

        while l < r:
            currArea = max(currArea, (r-l)*min(heights[l], heights[r]))
            print(currArea)

            if heights[l] < heights[r]:
                l += 1
            else:
                r-= 1
        
        return currArea
