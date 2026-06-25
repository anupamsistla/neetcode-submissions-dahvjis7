class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        res = []

        for i in range(len(intervals)):
            if not res:
                res.append(intervals[i])
            
            else:
                curr = res.pop()
                
                if curr[1] >= intervals[i][0]:
                    merged = [min(curr[0], intervals[i][0]), max(curr[1], intervals[i][1])]
                    res.append(merged)
                
                else:
                    res.append(curr)
                    res.append(intervals[i])
        return res    