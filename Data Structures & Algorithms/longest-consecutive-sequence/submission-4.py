class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        toCheck = set(nums)

        maxLen = 0
        for num in nums:
            currLen = 0
            if (num+1) not in toCheck:
                currLen = 1
                while (num-1) in toCheck:
                    num -= 1
                    currLen += 1
                maxLen = max(maxLen, currLen)
        
        return maxLen