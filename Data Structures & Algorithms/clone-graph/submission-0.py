"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return
        nodeClone = Node(node.val)
        cache = {}

        def dfs(root, rootClone):
            if not root:
                return
            cache[root] = rootClone

            for n in root.neighbors:
                
                nClone = cache.get(n, Node(n.val))
                rootClone.neighbors.append(nClone)
                if n not in cache:
                    dfs(n, nClone)
        
        dfs(node, nodeClone)

        return nodeClone