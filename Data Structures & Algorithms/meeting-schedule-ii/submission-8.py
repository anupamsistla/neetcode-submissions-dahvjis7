"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        numRooms = 0

        startTimes = [interval.start for interval in intervals]
        endTimes = [interval.end for interval in intervals]

        startTimes.sort()
        endTimes.sort()
        
        i1 = 0
        i2 = 0
        toRet = 0

        while i1 < len(intervals) and i2 < len(intervals):
            if startTimes[i1] < endTimes[i2]:
                numRooms += 1
                i1 += 1
            
            elif startTimes[i1] >= endTimes[i2]:
                numRooms -= 1
                i2 += 1
        
            toRet = max(toRet, numRooms)
        
        return toRet
