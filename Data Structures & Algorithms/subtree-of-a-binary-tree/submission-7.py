# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def sameTree(self, p, q):
        if not p and not q:
            return True

        if p and not q or q and not p:
            return False

        if p and q and p.val != q.val:
            return False

        return self.sameTree(p.left, q.left) and self.sameTree(p.right, q.right)
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        stack = list()
        stack.append(root)

        while stack:
            curr = stack.pop()

            if self.sameTree(curr, subRoot):
                return True 
            
            if curr.left:
                stack.append(curr.left)
            
            if curr.right:
                stack.append(curr.right)
        
        return False
