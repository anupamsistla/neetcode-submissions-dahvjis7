# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:

        #left threshold, right threshold
        self.flag = True
    
        def dfs(root, lowerLimit, upperLimit):
            if not root:
                return
            
            if root.val <= lowerLimit or root.val >= upperLimit:
                self.flag = False
            
            dfs(root.left, lowerLimit,root.val)
            dfs(root.right, root.val, upperLimit)
            return
        
        dfs(root, float("-inf"), float("inf"))
        return self.flag        
            
