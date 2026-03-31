class Solution:
    def maxArea(self, heights: List[int]) -> int:
        largest = 0
        l,r = 0, len(heights)-1

        while l < r:
            if(heights[l] > heights[r]):
                height = heights[r]*(r-l)
                largest = max(largest, height)
                r-=1

            else:
                height = heights[l]*(r-l)
                largest = max(largest, height)
                l+=1
        return largest