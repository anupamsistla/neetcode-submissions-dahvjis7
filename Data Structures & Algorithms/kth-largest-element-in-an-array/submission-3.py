class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        self.minHeap = []

        for num in nums:
            heapq.heappush(self.minHeap, num)

            if len(self.minHeap) > k:
                heapq.heappop(self.minHeap)

        return self.minHeap[0]
        