# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True

        def getLen(root, end):
            if not root:
                return 0
            if end[0] == False:
                return 0

            left = getLen(root.left, end)
            right = getLen(root.right, end)

            if abs(left - right) > 1:
                print("boom")
                end[0] = False
                return 0

            return 1 + max(left, right)

        end = [True]
        getLen(root, end)

        return end[0]

