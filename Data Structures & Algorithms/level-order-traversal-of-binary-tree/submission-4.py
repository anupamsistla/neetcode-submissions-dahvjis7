# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        res = defaultdict(list)

        def dfs(curr, depth):
            if not curr:
                return None
            
            res[depth].append(curr.val)

            dfs(curr.left, depth+1)
            dfs(curr.right, depth+1)
        
        dfs(root, 0)
        return list(res.values())

            
        
            

            
