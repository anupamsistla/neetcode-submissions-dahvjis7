class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        # take points and find their euclidean distance to the origin and put into minheap of size k, use negative weights so that i can pop till k
        # since i can return answer in any order, this should work

        nums = []
        # map for distance to point -> what if two points have the same distance?
        for point in points: # o(n)
            dist = math.sqrt(point[0]**2 + point[1]**2)
            heapq.heappush(nums, (-dist, point))

            if len(nums) > k:
                heapq.heappop(nums)
            
        
        return [p for _, p in nums]