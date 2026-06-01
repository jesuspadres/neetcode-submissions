# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        def traverse(root, minVal, maxVal):
            if not root:
                return True

            retVal = True

            if root.left:
                if root.left.val < root.val and root.left.val > minVal:
                    retVal = True
                else:
                    return False
                retVal = traverse(root.left, minVal, root.val)
            
            if root.right:
                if root.right.val > root.val and root.right.val < maxVal:
                    retVal = retVal and True
                else:
                    return False
                retVal = retVal and traverse(root.right, root.val, maxVal)

            return retVal

        return traverse(root, -1001, 1001)