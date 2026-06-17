class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.nums = nums
        self.k = k
        self.minHeap = []

        i = 0
        while i < len(nums):
            heapq.heappush(self.minHeap, nums[i])

            if len(self.minHeap) > k:
                heapq.heappop(self.minHeap)
            i += 1
        return

        

    def add(self, val: int) -> int:
        self.nums.append(val)
        heapq.heappush(self.minHeap, val)
        
        if len(self.minHeap) > self.k:
            heapq.heappop(self.minHeap)
        
        return self.minHeap[0]
