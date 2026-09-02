class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        rightGreatest = [0]*len(arr)
        maxR = -1
        for i in range(len(arr)-1, -1, -1):
            rightGreatest[i] = maxR
            maxR = max(maxR, arr[i])
        
        return rightGreatest