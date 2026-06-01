# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        indices = {val: idx for idx, val in enumerate(inorder)}
        
        def addNode(root, node, indices):
            if not root:
                return

            if indices[node.val] < indices[root.val]:
                if not root.left:
                    root.left = node
                else:
                    addNode(root.left, node, indices)
            elif indices[node.val] > indices[root.val]:
                if not root.right:
                    root.right = node
                else:
                    addNode(root.right, node, indices)

        tree = TreeNode(preorder[0])
        for i in range(1, len(preorder)):
            addNode(tree, TreeNode(preorder[i]), indices)

        return tree