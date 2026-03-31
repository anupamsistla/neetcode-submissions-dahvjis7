import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        #brute force solution using max heap
        counts = defaultdict(int)

        for n in nums:
            counts[n] = 0
        
        for n in nums:
            counts[n] += 1
        
        pq = []
        for key, value in counts.items():
            heapq.heappush(pq, (-value, key))

        res = []
        for i in range(k):
            _, key = heapq.heappop(pq)
            res.append(key)
        return res
