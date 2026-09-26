from collections import defaultdict
class TimeMap:

    def __init__(self):
        self.Map = defaultdict(list)

        

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.Map[key].append((timestamp, value))
        

    def get(self, key: str, timestamp: int) -> str:
        # use binary search for getting the closest timestamp value to timestamp
        if not key in self.Map:
            return ""

        l,r = 0, len(self.Map[key])-1

        while l <= r:
            mid = (l+r)//2

            if self.Map[key][mid][0] == timestamp:
                return self.Map[key][mid][1]

            elif self.Map[key][mid][0] < timestamp:
                l = mid + 1
            
            else:
                r = mid - 1
        

        return self.Map[key][r][1] if self.Map[key][r][0] <= timestamp else ""
        
        
