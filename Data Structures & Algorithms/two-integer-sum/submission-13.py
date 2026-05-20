class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        res = dict()

        for i, n in enumerate(nums):
            toFind = target - n

            if toFind in res:
                return [res[toFind], i]
            
            if n not in res:
                res[n] = i
        
        return []