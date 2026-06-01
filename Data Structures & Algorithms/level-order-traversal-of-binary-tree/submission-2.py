# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        retVal = []

        def dst(curr, height):
            if not curr:
                return 
            if height >= len(retVal):
                retVal.append([])

            retVal[height].append(curr.val)

            dst(curr.left, height+1)
            dst(curr.right, height+1)

        dst(root, 0)

        return retVal