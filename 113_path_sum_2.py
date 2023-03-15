# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        output = []
        if not root:return output
        if not root.left and not root.right:
            if root.val == targetSum:
                output.append([root.val])
                return output


        def treverse(root,path,temp_sum):
            temp = path[:]
            temp.append(root.val)
            temp_sum += root.val
            if root.left:
                treverse(root.left,temp,temp_sum)
            if root.right:
                treverse(root.right,temp,temp_sum)
            if not root.left and not root.right and targetSum == temp_sum:
                output.append(temp)
            
        
        treverse(root,[],0)
        return output