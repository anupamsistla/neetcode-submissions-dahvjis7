class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # mySet = set()
        # for i in nums:
        #     if i in mySet:
        #         return True
        #     mySet.add(i)
        # return False

        mySet = set()
        for i in nums:
            mySet.add(i)
        return len(mySet) != len(nums)