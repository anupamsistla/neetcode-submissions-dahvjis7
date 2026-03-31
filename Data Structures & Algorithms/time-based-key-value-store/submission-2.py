class TimeMap:

    def __init__(self):
        self.myDict = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.myDict[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        values = self.myDict[key]
        if not values:
            return ""
        l,r = 0, len(values)-1
        check = values[l]
        large = values[l][0]
        while(l<=r):
            mid = (l+r)//2
            if(values[mid][0] <= timestamp):
                large = max(large, values[mid][0])
                check = values[mid]
                l = mid + 1
            else:
                r = mid - 1
            
        if not check[0] <= timestamp:
            return ""
        
        return check[1]
        
        


