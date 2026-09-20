import heapq
class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        trips.sort(key = lambda t: t[1])

        minHeap = [] # [end, numPass]
        currPassen = 0

        for t in trips:
            passen, start, end = t

            while minHeap and start >= minHeap[0][0]:
                prevPassen = minHeap[0][1]
                currPassen -= prevPassen
                heapq.heappop(minHeap)
            
            currPassen += passen
            
            if currPassen > capacity:
                return False

            heapq.heappush(minHeap, (end, passen))

        return True










            
        
