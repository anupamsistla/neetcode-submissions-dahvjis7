# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        self.flag = True

        def dfs(root, lowerLimit, upperLimit):
            if not root:
                return

            if not root.val > lowerLimit or not root.val < upperLimit:
                self.flag = False
            
            dfs(root.left, lowerLimit, root.val)
            dfs(root.right, root.val, upperLimit)
        
        dfs(root, float("-inf"), float("inf"))
        return self.flag


            