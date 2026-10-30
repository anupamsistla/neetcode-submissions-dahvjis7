class Solution:
    def findMinArrowShots(self, points: list[list[int]]) -> int:
        res = 0
        points.sort()
        prevEnd = points[0][1]

        for start, end in points[1:]:
            if start > prevEnd:
                prevEnd = end
            
            else:
                res += 1
                prevEnd = min(prevEnd, end)
        
        return len(points) - res