import heapq
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        maxHeap = []

        for stone in stones:
            heapq.heappush(maxHeap, -stone)

        while len(maxHeap) > 1:
            first = -heapq.heappop(maxHeap)
            second = -heapq.heappop(maxHeap)

            res = abs(first) - abs(second)

            if res > 0:
                heapq.heappush(maxHeap, -res)
            
    
        if maxHeap:
            return -maxHeap[0]
        else:
            return 0
