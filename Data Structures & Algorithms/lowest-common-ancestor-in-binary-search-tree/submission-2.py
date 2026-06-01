# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        def contains(root, node):
            if not root:
                return False

            q = deque([root])

            while q:
                curr = q.popleft()

                if curr.val == node.val:
                    return True

                if curr.left:
                    q.append(curr.left)
                if curr.right:
                    q.append(curr.right)

            return False

        
        que = deque([root])

        retVal = root

        while que:
            curr = que.popleft()

            if contains(curr, p) and contains(curr, q):
                retVal = curr

            if curr.left:
                que.append(curr.left)
            if curr.right:
                que.append(curr.right)

        return retVal
