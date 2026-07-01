import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        minHeap = []
        count = {}
        for num in nums:
            count[num] = 1 + count.get(num,0)
        
        for key, value in count.items():
            minHeap.append((-value, key))
        
        heapq.heapify(minHeap)

        i = 0
        res = []
        while i < k:
            _, curr = heapq.heappop(minHeap)
            res.append(curr)
            i+=1
        return res
        # 1 2 2 3 3

