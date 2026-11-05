# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def leafSimilar(self, root1: TreeNode | None, root2: TreeNode | None) -> bool:
        def getSequence(curr, res):
            if not curr:
                return
            
            if not curr.left and not curr.right:
                res.append(curr.val)
                return
            
            getSequence(curr.left, res)
            getSequence(curr.right, res)

        res1 = []
        res2 = []

        getSequence(root1, res1)
        getSequence(root2, res2)

        return res1 == res2
