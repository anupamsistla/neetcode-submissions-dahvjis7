# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        # level order traversal
        # all right
        if not root:
            return []
        res = []
        queue = deque()
        queue.append(root)

        while queue:
            for i in range(len(queue)):
                curr = queue.popleft()

                if curr.left:
                    queue.append(curr.left)
                
                if curr.right:
                    queue.append(curr.right)
                
            res.append(curr.val)
        
        return res