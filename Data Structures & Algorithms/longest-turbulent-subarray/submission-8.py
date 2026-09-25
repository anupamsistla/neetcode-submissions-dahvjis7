class Solution:
    def maxTurbulenceSize(self, arr: List[int]) -> int:
        prev = ""
        maxSize = 1

        l,r = 0, 1

        while r < len(arr):
            if arr[r] > arr[r-1] and prev != ">":
                prev = ">"
                maxSize = max(maxSize, r-l+1)
                r += 1
            
            elif arr[r] < arr[r-1] and prev != "<":
                prev = "<"
                maxSize = max(maxSize, r-l+1)
                r += 1
            
            else:
                prev = ""
                r = r + 1 if arr[r] == arr[r-1] else r
                l = r - 1
            
        
        return maxSize
