# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        tMap = {}

        def traverse(root, level, map):
            if not root:
                return

            map[level] = map.get(level, [])
            map[level].append(root.val)

            traverse(root.left, level+1, map)
            traverse(root.right, level+1, map)

        traverse(root, 0, tMap)

        retVal = []
        for i in range(len(tMap)):
            retVal.append(tMap[i])

        return retVal