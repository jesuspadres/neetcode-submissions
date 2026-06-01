# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        retVal = [root.val]

        def helper(root, retVal):
            if not root:
                return -1101

            currVal = otherVal = root.val
            lVal = helper(root.left, retVal)
            rVal = helper(root.right, retVal)

            if lVal > 0:
                currVal += lVal
                otherVal += lVal
            if rVal > 0:
                currVal += rVal
                if rVal > lVal and lVal > 0:
                    otherVal = otherVal - lVal + rVal
                elif rVal > lVal:
                    otherVal = otherVal + rVal

            print(otherVal, currVal)
            retVal[0] = max(retVal[0], currVal, rVal, lVal)

            return otherVal

        helper(root, retVal)

        return retVal[0]