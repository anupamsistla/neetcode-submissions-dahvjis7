class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        currSum = sum(nums)

        if currSum % k != 0:
            return False

        used = [False] * len(nums)
        target = currSum // k
        nums.sort(reverse = True)
    
        def backtrack(i, k, subsetSum):
            if k == 0:
                return True
            
            if subsetSum == target:
                return backtrack(0, k-1, 0)
            
            for j in range(i, len(nums)):
                if used[j] or nums[j] + subsetSum > target:
                    continue
                
                used[j] = True
                if backtrack(j+1, k, subsetSum + nums[j]):
                    return True 
                
                used[j] = False

                if subsetSum == 0:
                    return False
            
            return False
        
        return backtrack(0, k, 0)
            