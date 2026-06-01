# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        

        def traverse(root, maxVal):
            if not root:
                return 0

            retVal = 0

            if root.val >= maxVal:
                maxVal = max(maxVal, root.val)
                retVal = 1

            return retVal + traverse(root.left, maxVal) + traverse(root.right, maxVal)

        return traverse(root, -101)