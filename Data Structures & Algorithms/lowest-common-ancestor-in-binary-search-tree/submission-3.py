# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        maxVal = max(p.val, q.val)
        minVal = min(p.val, q.val)

        while True:
            if (root.val < maxVal and root.val > minVal) or root.val in (maxVal, minVal):
                return root
            elif root.val < minVal:
                root = root.right
            else:
                root = root.left

        return root
