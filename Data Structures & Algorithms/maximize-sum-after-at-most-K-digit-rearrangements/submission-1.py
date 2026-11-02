class Solution:
    def maximizeSum(self, nums: list[int], k: int) -> int:
        minHeap = []

        for i, num in enumerate(nums):
            sorted_chars = sorted(str(num), reverse=True)
            value = int("".join(sorted_chars))
            diff = value - num

            if diff > 0:    
                heapq.heappush(minHeap, (diff, value, i))

            if len(minHeap) > k:
                heapq.heappop(minHeap)
    

        while minHeap:
            diff, value, i = heapq.heappop(minHeap)
            nums[i] = value
        
        return sum(nums)