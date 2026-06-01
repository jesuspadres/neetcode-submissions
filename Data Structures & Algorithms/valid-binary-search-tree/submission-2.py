# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:

        retVal = True
        
        def dfs(node, minVal, maxVal):
            nonlocal retVal
            if not node:
                return 

            if node.val <= minVal or node.val >= maxVal:
                retVal = False
                return

            dfs(node.left, minVal, node.val)
            dfs(node.right, node.val, maxVal)

        dfs(root, -1001, 1001)

        return retVal