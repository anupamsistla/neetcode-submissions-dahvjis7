class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l,r = 1, max(piles)
        minRes = max(piles)

        while l <= r:
            mid = (l+r)//2

            calc = 0
            for p in piles:
                calc += math.ceil(p/mid)
            
            if calc <= h:
                minRes = min(minRes, mid)
                r = mid - 1
            
            else:
                l = mid + 1
        
        return minRes
        





