# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        returns = []
        def helper(root, p, q, retVal):
            if retVal != []:
                return set()
            if root == None:
                return set()

            nSet = set()
            nSet.add(root.val)
            nSet.update(helper(root.left, p, q, retVal))
            nSet.update(helper(root.right, p, q, retVal))

            if p.val in nSet and q.val in nSet and retVal == []:
                retVal.append(root)

            return nSet
            
        helper(root, p, q, returns)

        return returns[0]
