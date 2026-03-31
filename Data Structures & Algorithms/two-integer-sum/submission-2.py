class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # prevMap = {}
        # for i, n in enumerate(nums):
        #     diff = target - n
        #     if diff in prevMap:
        #         return [prevMap[diff], i]
        #     prevMap[n] = i
        
        indices = {}

        for i, n in enumerate(nums):
            indices[n] = i

        for j in range(len(nums)):
            toFind = target-nums[j]
            if toFind in indices and indices[toFind] != j:
                return[j,indices[toFind]]
        


        
        