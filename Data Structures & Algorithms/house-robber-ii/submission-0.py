class Solution:
    def foo(self, nums):
        prev = nums[0]
        prev2 = 0
        n = len(nums)

        for i in range(1, n):
            pick = prev2 + nums[i]
            notPick = prev
            prev2 = prev
            prev = max(pick, notPick)
        
        return prev

    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return nums[0]

        temp1 = nums[:n-1]
        temp2 = nums[1:]

        return max(self.foo(temp1), self.foo(temp2))
        