# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        retVal = 0
        
        def helper(root, maxVal):
            nonlocal retVal
            if not root:
                return

            if root.val >= maxVal:
                retVal += 1

            maxVal = max(maxVal, root.val)

            helper(root.left, maxVal)
            helper(root.right, maxVal)

        helper(root, -100)

        return retVal