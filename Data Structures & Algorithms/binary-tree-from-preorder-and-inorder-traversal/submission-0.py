# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        
        def addNode(root, node, inOrder):
            if not root:
                return

            if inOrder.index(node.val) < inOrder.index(root.val):
                if not root.left:
                    root.left = node
                else:
                    addNode(root.left, node, inOrder)
            elif inOrder.index(node.val) > inOrder.index(root.val):
                if not root.right:
                    root.right = node
                else:
                    addNode(root.right, node, inOrder)

        tree = TreeNode(preorder[0])
        for i in range(1, len(preorder)):
            addNode(tree, TreeNode(preorder[i]), inorder)

        return tree