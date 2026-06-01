# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        def helper(root, orderedList):
            if not root:
                return

            helper(root.left, orderedList)
            orderedList.append(root.val)
            helper(root.right, orderedList)

        orderedList = []
        helper(root, orderedList)

        for i in range(1, len(orderedList)):
            if orderedList[i-1] >= orderedList[i]:
                return False

        return True