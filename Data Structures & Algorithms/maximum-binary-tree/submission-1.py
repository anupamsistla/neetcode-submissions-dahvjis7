# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def constructMaximumBinaryTree(self, nums: list[int]) -> TreeNode | None:
        def foo(nums):
            if not nums:
                return None
            
            maxNum = max(nums)
            maxI = nums.index(maxNum)
        
            root = TreeNode(maxNum)
            root.left = foo(nums[:maxI])
            root.right = foo(nums[maxI+1:])
            return root
        
        return foo(nums)