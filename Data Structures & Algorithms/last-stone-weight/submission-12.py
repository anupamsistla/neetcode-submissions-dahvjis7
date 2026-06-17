class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        if len(stones) == 1:
            return stones[0]
        
        if not stones:
            return 0 
        maxHeap = []

        for s in stones:
            heapq.heappush(maxHeap, -s)
    
        while len(maxHeap) > 1:
            x = -heapq.heappop(maxHeap)
            y = -heapq.heappop(maxHeap)

            res = abs(x - y)
            heapq.heappush(maxHeap, -res)
        
        return -maxHeap[0]