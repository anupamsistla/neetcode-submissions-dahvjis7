import heapq
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []

        for x, y in points:
            distToOrigin = math.sqrt(x**2 + y** 2)
            heapq.heappush(heap, (-distToOrigin, (x, y)))

            if len(heap) > k:
                heapq.heappop(heap)

        toRet = []
        for _, point in heap:
            toRet.append(point)
        
        return toRet