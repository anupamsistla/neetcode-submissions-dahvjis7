# """
# This is MountainArray's API interface.
# You should not implement it, or speculate about its implementation
# """
#class MountainArray:
#    def get(self, index: int) -> int:
#    def length(self) -> int:

class Solution:
    def findInMountainArray(self, target: int, mountainArr: 'MountainArray') -> int:
        length = mountainArr.length()
        l,r = 1, length-2

        while l <= r:
            m = (l+r)//2

            left, mid, right = mountainArr.get(m-1), mountainArr.get(m), mountainArr.get(m+1)

            if left < mid < right:
                l = m + 1
            
            elif left > mid > right:
                r = m - 1
            
            else:
                break
            
        peak = m
        l, r = 0, peak

        while l <= r:
            m = (l+r)//2

            mid = mountainArr.get(m)

            if mid == target:
                return m
            
            elif mid < target:
                l = m + 1
            
            else:
                r = m - 1
        
        l,r = peak, length - 1
        while l <= r:
            m = (l+r)//2

            mid = mountainArr.get(m)

            if mid == target:
                return m
            
            elif mid > target:
                l = m + 1
            
            else:
                r = m - 1
        
        return -1