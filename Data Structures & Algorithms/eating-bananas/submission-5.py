class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # Binary search from largest pile in piles

        l,r = 1, max(piles)
        minRate = max(piles)
        while l <= r:
            eatingRate = (l+r)//2

            res = 0
            for p in piles:
                res += math.ceil(p/eatingRate)
            
            if res > h:
                l = eatingRate + 1

            else:
                minRate = min(minRate, eatingRate)
                r = eatingRate - 1

    
        return minRate