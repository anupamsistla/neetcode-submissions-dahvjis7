class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        maxPile = max(piles)

        l,r  = 1, maxPile

        res = 0
        while l <= r:
            mid = (l+r)//2
            check = 0

            for p in piles:
                check += math.ceil(p/mid)

            if check > h:
                l = mid + 1
            elif check <= h:
                res = mid
                r = mid - 1
        return res


            
            



                
