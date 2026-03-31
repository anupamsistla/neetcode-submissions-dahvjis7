class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        output = []

        temp = 1

        for i in range(len(nums)):
            output.append(temp)
            temp = temp * nums[i]
        
        temp = 1
        for i in range(len(nums)-1, -1, -1):
            output[i] = output[i]* temp
            temp = temp*nums[i]

        return output