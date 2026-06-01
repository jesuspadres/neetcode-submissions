class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        
        class Node:
            def __init__(self, val):
                self.val = val
                self.children = []

        nodes = [Node(i) for i in range(n)]

        for edge in edges:
            n1 = edge[0]
            n2 = edge[1]

            nodes[n1].children.append(nodes[n2])
            nodes[n2].children.append(nodes[n1])

        visited = set()

        def dfs(currNode, prevNode):
            if currNode in visited:
                return False

            visited.add(currNode)
            for node in currNode.children:
                if node != prevNode:
                    if not dfs(node, currNode):
                        return False

            return True

        tree = dfs(nodes[0], None)

        if len(visited) == n and tree:
            return True

        return False

