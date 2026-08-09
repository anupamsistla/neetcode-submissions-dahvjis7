class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        minCap = totSum = sum(weights)

        l,r = 0, minCap

        while l <= r:
            mid = (l+r)//2

            numDays = 1
            currCap = mid
            
            for w in weights:
                if w > mid:
                    numDays = float("inf")

                elif w <= currCap:
                    currCap -= w

                else:
                    numDays += 1
                    currCap = mid - w

            if numDays <= days:
                r = mid - 1 
                minCap = min(minCap, mid)
            
            else:
                l = mid + 1

        return minCap
            

