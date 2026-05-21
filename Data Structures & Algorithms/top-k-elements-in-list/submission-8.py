import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        heap = []

        count = {}

        for num in nums:
            count[num] = 1 + count.get(num, 0)

        for key, value in count.items():
            heapq.heappush(heap, (value, key))

        while len(heap) > k:
            heapq.heappop(heap)

        return [tup[1] for tup in heap]

