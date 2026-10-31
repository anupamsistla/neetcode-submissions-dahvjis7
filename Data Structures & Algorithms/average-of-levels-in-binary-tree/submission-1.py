# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def averageOfLevels(self, root: TreeNode | None) -> list[float]:
        queue = deque()
        queue.append(root)
        res = []

        while queue:
            currLevel = 0
            numNodes = len(queue)
            for i in range(len(queue)):
                curr = queue.popleft()
                currLevel += curr.val
                
                if curr.left:
                    queue.append(curr.left)
                
                if curr.right:
                    queue.append(curr.right)
            
            res.append(currLevel/numNodes)
        
        return res

