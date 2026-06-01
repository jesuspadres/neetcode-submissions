# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        def helper(root, level, lists):
            if not root:
                return

            if level >= len(lists):
                lists.append([])

            lists[level].append(root.val)

            helper(root.left, level+1, lists)
            helper(root.right, level+1, lists)

        retVal = []
        helper(root, 0, retVal)

        return retVal