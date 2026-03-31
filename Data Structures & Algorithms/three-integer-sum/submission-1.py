class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        solutions = []
        nums.sort()
        for i, n in enumerate(nums):
            if(i>0 and nums[i-1] == n):
                continue
            l,r = i+1, len(nums)-1
            while l < r:
                target = n + nums[l] + nums[r]
                if(target < 0):
                    l+=1
                elif(target > 0):
                    r-=1
                else:
                    solutions.append([n, nums[l], nums[r]])
                    l+=1
                    while(nums[l-1] == nums[l] and l < r):
                        l+=1
        return solutions 