class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        triangle = []

        count = 1
        while count <= numRows:
            triangle.append([1]*count)
            count += 1
        
        for i in range(numRows):
            for j in range(len(triangle[i])):
                if (j-1) in range(len(triangle[i-1])) and j in range(len(triangle[i-1])):
                    triangle[i][j] = triangle[i-1][j-1] + triangle[i-1][j]
    
        return triangle