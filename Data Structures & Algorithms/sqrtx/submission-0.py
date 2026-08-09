class Solution:
    def mySqrt(self, x: int) -> int:
        l,r = 0, x

        while l <= r:
            mid = (l+r)//2

            res = mid * mid 

            if res == x:
                return mid
            
            elif res < x:
                l = mid + 1
            
            else:
                r = mid - 1
        
        return l-1