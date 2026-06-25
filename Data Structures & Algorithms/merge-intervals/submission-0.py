class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        res = []

        for i in range(len(intervals)):
            flag = False
            if not res:
                res.append(intervals[i])
                flag = True
            
            else:
                curr = res.pop()
                
                if curr[1] >= intervals[i][0]:
                    curr = [min(curr[0], intervals[i][0]), max(curr[1], intervals[i][1])]
                    flag = True

                res.append(curr)
            
            if not flag:
                res.append(intervals[i])
        return res            