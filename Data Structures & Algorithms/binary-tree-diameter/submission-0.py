# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        retVal = [0]
        self.traverse(root, retVal)

        return retVal[0]

    def traverse(self, root, retVal):
        if not root:
            return 0
        
        hLeft = self.traverse(root.left, retVal)
        hRight = self.traverse(root.right, retVal)

        retVal[0] = max(retVal[0], hLeft + hRight)

        return max(hLeft, hRight) + 1
