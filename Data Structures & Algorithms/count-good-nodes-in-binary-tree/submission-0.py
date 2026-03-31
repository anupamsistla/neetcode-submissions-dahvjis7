# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        self.good = 0
        def dfs(root, maxNode):
            if not root:
                return None
            
            if root.val >= maxNode:
                maxNode = root.val
                self.good+=1
            
            dfs(root.left, maxNode)
            dfs(root.right, maxNode)
        
        dfs(root, float("-inf"))
        return self.good