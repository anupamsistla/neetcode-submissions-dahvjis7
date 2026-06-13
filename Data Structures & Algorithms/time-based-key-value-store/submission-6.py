from collections import defaultdict
class TimeMap:

    def __init__(self):
        self.mapping = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.mapping[key].append((value, timestamp))

    def get(self, key: str, timestamp: int) -> str:
        # lets say I'm given a time stamp, use binary search to find the timestamp that is stored
        # whose time stamp is the largest that is <= my timestamp

        tupList = self.mapping[key]

        l,r = 0, len(tupList)-1
        minTimestamp = float("inf")
        minValue = None
        while l <= r:
            mid = (l+r)//2

            if tupList[mid][1] <= timestamp:
                minTimestamp = min(minTimestamp, tupList[mid][1])
                minValue = tupList[mid][0]
                l = mid + 1
            
            else:
                r = mid - 1

        return minValue if minValue else ""





