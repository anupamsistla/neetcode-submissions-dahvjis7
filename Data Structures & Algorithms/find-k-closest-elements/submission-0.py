from collections import deque
class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        l,r = 0, 0
        res = deque()

        while r < len(arr):
            if len(res) == k and (abs(res[0] - x) > abs(arr[r] - x)):
                res.popleft()
            
            if len(res) < k:
                res.append(arr[r])
            r += 1
        
        return list(res)