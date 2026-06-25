class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        res = [intervals[0]]

        for i in range(1, len(intervals)):
            curr = res.pop()
            
            if curr[1] >= intervals[i][0]:
                merged = [min(curr[0], intervals[i][0]), max(curr[1], intervals[i][1])]
                res.append(merged)
            
            else:
                res.append(curr)
                res.append(intervals[i])
        return res    