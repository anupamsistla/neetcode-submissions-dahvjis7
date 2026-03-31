class TimeMap:

    def __init__(self):
        self.mapping = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.mapping[key].append((value, timestamp))
        

    def get(self, key: str, timestamp: int) -> str:
        if not self.mapping[key]:
            return ""

        l,r = 0, len(self.mapping[key])-1

        while l <= r:
            mid = (l+r)//2

            if self.mapping[key][mid][1] == timestamp:
                return self.mapping[key][mid][0]

            elif self.mapping[key][mid][1] > timestamp:
                r = mid - 1
            
            else:
                l = mid + 1
        
        if self.mapping[key][r][1] <= timestamp:
            return self.mapping[key][r][0]
        else:
            return ""
        
