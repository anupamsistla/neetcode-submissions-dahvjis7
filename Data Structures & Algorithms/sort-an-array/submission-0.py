class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        minHeap = []
        
        for num in nums:
            heapq.heappush(minHeap, num)
        
        res = []

        while minHeap:
            res.append(heapq.heappop(minHeap))
    
        return res