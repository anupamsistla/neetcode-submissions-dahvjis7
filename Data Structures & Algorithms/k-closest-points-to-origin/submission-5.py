class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        self.maxHeap = []

        for p in points:
            res = -math.sqrt(math.pow(abs(p[0]), 2) + math.pow(abs(p[1]), 2))
            heapq.heappush(self.maxHeap, (res, p))
            if len(self.maxHeap) > k:
                heapq.heappop(self.maxHeap)
        
        return [p[1] for p in self.maxHeap]
            