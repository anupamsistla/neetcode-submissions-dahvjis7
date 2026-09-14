# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        self.count = 0
        
        def dfs(root, prevMax):
            if not root:
                return None
            
            if root.val >= prevMax:
                self.count += 1
                prevMax = max(prevMax, root.val)
            
            dfs(root.left, prevMax)
            dfs(root.right, prevMax)

        dfs(root, root.val)
        return self.count
            