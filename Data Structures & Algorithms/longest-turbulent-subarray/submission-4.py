class Solution:
    def maxTurbulenceSize(self, arr: List[int]) -> int:
        prev = ""
        l,r = 0, 0
        maxSize = 1

        while r < len(arr)-1:
            if arr[r] > arr[r+1] and (prev == "<" or prev == ""):
                prev = ">"
                r += 1
                maxSize = max(maxSize, r-l+1)
            
            elif arr[r] < arr[r+1] and (prev == ">" or prev == ""):
                prev = "<"
                r += 1
                maxSize = max(maxSize, r-l+1)
            
            else:
                prev = ""
                r = r + 1 if arr[r] == arr[r+1] else r
                l = r
                
        
        return maxSize