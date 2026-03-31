class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        maxHeap = []

        for stone in stones:
            maxHeap.append(-stone)
        
        heapq.heapify(maxHeap)
    
        while len(maxHeap) > 1:
            one = heapq.heappop(maxHeap)
            one = abs(one)

            two = heapq.heappop(maxHeap)
            two = abs(two)
        
            if one != two:
                three = abs(two - one)
                heapq.heappush(maxHeap, -three)
        
        
        return abs(maxHeap[0]) if maxHeap else 0