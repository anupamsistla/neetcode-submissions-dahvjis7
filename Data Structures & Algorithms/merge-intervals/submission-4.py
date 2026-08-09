class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        stack = []

        for i in range(len(intervals)):
            if not stack:
                stack.append(intervals[i])
            
            else:
                if stack and stack[-1][1] >= intervals[i][0]:
                    prevInterval = stack.pop()
                    newInterval = [min(prevInterval[0], intervals[i][0]), max(prevInterval[1], intervals[i][1])]
                    stack.append(newInterval)
                
                else:
                    stack.append(intervals[i])
    
        return stack