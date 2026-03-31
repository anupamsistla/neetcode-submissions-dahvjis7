class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        for i in range(len(numbers)):
            search = target - numbers[i]
            j = i+1
            while search in numbers or j<len(numbers):
                if(numbers[j] == search):
                    return [i+1,j+1]
                j+=1



        