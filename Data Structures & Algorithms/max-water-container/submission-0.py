class Solution:
    def maxArea(self, heights: List[int]) -> int:
        largest = 0
        l,r = 0, len(heights)-1

        while(l<r):
            if(heights[l] > heights[r]):
                check = heights[r] * (r-l)
                largest = max(largest, check)
                r -= 1
            elif(heights[l] <= heights[r]):
                check = heights[l] * (r-l)
                largest = max(largest, check)
                l += 1
        return largest
