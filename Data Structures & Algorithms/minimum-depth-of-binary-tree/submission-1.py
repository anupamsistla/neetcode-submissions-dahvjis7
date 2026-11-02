# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: TreeNode | None) -> int:
        if not root:
            return 0

        def foo(root):
            if not root:
                return float("inf") 

            if not root.left and not root.right:
                return 1
                
            left = foo(root.left)
            right = foo(root.right)
            return 1 + min(left, right)
        
        return foo(root)