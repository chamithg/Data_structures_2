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
        if root.val == targetSum and not root.left and not root.left:
            output.append([root.val])

        def treverse(root,temp):
            temp1 = temp[:]
            print(sum(temp1))
            if not root:
                if sum(temp1)== targetSum and len(temp1) >1:
                    if temp1 not in output:
                        output.append(temp1)
                return
            
            temp1.append(root.val)
            print(temp)
            treverse(root.left,temp1)
            treverse(root.right,temp1)
        
        treverse(root,[])
        return output