class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        for i in range(len(numbers)):
            search = target-numbers[i]
            j = 0
            if search in numbers:
                while numbers[j] != search and j < len(numbers):
                    j += 1
                return [i +1, j + 1]
        return []
                
            
                
