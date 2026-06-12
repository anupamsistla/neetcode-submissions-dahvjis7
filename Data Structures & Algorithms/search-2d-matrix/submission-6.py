class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        lMain, rMain = 0, len(matrix)-1

        while lMain <= rMain:
            midMain = (lMain + rMain)//2

            if target >= matrix[midMain][0] and target <= matrix[midMain][-1]:
                l,r = 0, len(matrix[midMain])-1

                while l <= r:
                    mid = (l+r)//2
                
                    if matrix[midMain][mid] == target:
                        return True
                    
                    elif matrix[midMain][mid] > target:
                        r = mid - 1
                    
                    else:
                        l = mid + 1
                return False
            
            elif target < matrix[midMain][0]:
                rMain = midMain - 1
            
            elif target > matrix[midMain][-1]:
                lMain = midMain + 1
        
        return False