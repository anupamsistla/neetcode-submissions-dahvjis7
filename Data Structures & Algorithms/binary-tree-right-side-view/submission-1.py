# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        q = deque()
        q.append(root)
        res = []

        while q:
            currLevel = []
            for i in range(len(q)):
                curr = q.popleft()
                currLevel.append(curr.val)
                
                if curr.left:
                    q.append(curr.left)
                
                if curr.right:
                    q.append(curr.right)
            
        
            res.append(currLevel)
        
        toRet = []

        for arr in res:
            toRet.append(arr[-1])
        
        return toRet

                