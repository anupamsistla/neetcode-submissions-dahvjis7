class TimeMap:

    def __init__(self):
        self.mapping = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.mapping[key].append((value, timestamp))
        

    def get(self, key: str, timestamp: int) -> str:
        if not self.mapping[key]:
            return ""
        for value, prevtimestamp in self.mapping[key][::-1]:
            if prevtimestamp <= timestamp:
                return value
    
        return ""
        
