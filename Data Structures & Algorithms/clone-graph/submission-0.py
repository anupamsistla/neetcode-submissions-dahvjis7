"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""
# Node with val and [Node1, Node2]
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        nodeToNew = {}

        def dfs(node):
            if node in nodeToNew:
                return nodeToNew[node]
        
            copy = Node(node.val)
            nodeToNew[node] = copy

            for nei in node.neighbors:
                copy.neighbors.append(dfs(nei))
        
            return copy
        
        return dfs(node) if node else None