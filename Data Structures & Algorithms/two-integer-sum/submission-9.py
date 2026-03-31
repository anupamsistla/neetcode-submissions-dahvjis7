class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        res = dict()

        for i in range(len(nums)):
            res[nums[i]] = i
        
        for i in range(len(nums)):
            toFind = target - nums[i]
        
            if toFind in res and i != res[toFind]:
                return [i, res[toFind]]
        

            