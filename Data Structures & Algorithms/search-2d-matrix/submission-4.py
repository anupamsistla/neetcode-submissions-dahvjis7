class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        lBig,rBig = 0, len(matrix)-1
        indexToCheck = -1
        while lBig <= rBig:
            midBig = (lBig+rBig)//2
            
            if target >= matrix[midBig][0] and target <= matrix[midBig][-1]:
                indexToCheck = midBig
                break
            
            elif target > matrix[midBig][-1]:
                lBig = midBig + 1
        
            elif target < matrix[midBig][0]:
                rBig = midBig - 1
        
    
        if midBig == -1:
            return False 
        
        l,r = 0, len(matrix[midBig])-1

        while l <= r:
            mid = (l+r)//2

            if matrix[midBig][mid] > target:
                r = mid -1
            
            elif matrix[midBig][mid] < target:
                l = mid + 1
            
            else:
                return True
        
        return False