class Solution:
    def foo(self, perm, nums, res):
        if len(perm) == len(nums):
            res.add(tuple(perm))
            return

        for i in range(len(nums)):
            if nums[i] != float("-inf"):
                perm.append(nums[i])
                nums[i] = float("-inf")
                self.foo(perm, nums, res)
                nums[i] = perm[-1]
                perm.pop()
        return 

    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        hashSet = set()
        self.foo([], nums, hashSet)
        res = []

        for perm in hashSet:
            res.append(list(perm))

        return res