import heapq
class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        trips.sort(key = lambda t:t[1])
        currCap = 0
        minHeap = []

        for t in trips:
            cap, start, end = t

            while minHeap and start >= minHeap[0][0]:
                currCap -= minHeap[0][1]
                heapq.heappop(minHeap)
            
            currCap += cap

            if currCap > capacity:
                return False
            
            heapq.heappush(minHeap, (end, cap))
        
        return True












            
        
