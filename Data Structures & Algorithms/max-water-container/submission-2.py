class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l = 0
        r = len(heights)-1

        maxVolume = 0
        while l < r:
            h = min(heights[l], heights[r])
            width = r - l

            volume = h * width
            maxVolume = max(maxVolume, volume)

            if heights[l] < heights[r]:
                l += 1
            else:
                r-=1
            
        return maxVolume
            
