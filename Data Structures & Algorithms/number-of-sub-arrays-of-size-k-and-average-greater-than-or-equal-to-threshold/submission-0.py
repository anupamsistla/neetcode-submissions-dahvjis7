class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        l,r = 0, 0
        currSum = 0
        count = 0

        while r < len(arr):
            currSum += arr[r]
            if (r-l+1) == k and currSum // k >= threshold:
                count += 1
                currSum -= arr[l]
                l += 1
            
            elif (r-l+1) == k and currSum // k < threshold:
                currSum -= arr[l]
                l += 1
            
            r += 1
    
        return count