# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':

        self.lca =None


        def dfs(node):
            if not node:
                return
            left = dfs(node.left)
            right = dfs(node.right)
        
            cur = node==p or node==q
            if (left and right) or (cur and right) or (cur and left):
                self.lca = node
                return 
            return left or right or cur

        dfs(root)
        return self.lca