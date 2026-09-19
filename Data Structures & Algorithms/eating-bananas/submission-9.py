class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:  
        l,r = 1, max(piles)
        minK = max(piles)


        while l <= r:
            mid = (l+r)//2
            
            currTime = 0
            for p in piles:
                currTime += math.ceil(p/mid)
                
            if currTime <= h:
                minK = min(minK, mid)
                r = mid -1

            else:
                l = mid +  1

        return minK

