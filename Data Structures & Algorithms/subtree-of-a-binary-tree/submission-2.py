# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        
        def isEqual(root1, root2):
            if not root1 and not root2:
                return True
            if root1 and root2:
                return root1.val == root2.val and isEqual(root1.left, root2.left) and isEqual(root1.right, root2.right)
            else:
                return False

        q = deque()

        q.append(root)
        retVal = False

        while q:
            node = q.popleft()

            if node.val == subRoot.val:
                retVal = isEqual(node, subRoot)

            if retVal:
                break

            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)

        return retVal