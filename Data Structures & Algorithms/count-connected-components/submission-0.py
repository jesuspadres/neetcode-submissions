class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        class Node:
            def __init__(self, val):
                self.val = val
                self.children = []

        nodes = [Node(i) for i in range(n)]

        for edge in edges:
            n1 = nodes[edge[0]]
            n2 = nodes[edge[1]]

            n1.children.append(n2)
            n2.children.append(n1)

        visited = set()

        def dfs(node):
            if node in visited:
                return

            visited.add(node)

            for child in node.children:
                dfs(child)

        retVal = 0
        for node in nodes:
            if node not in visited:
                dfs(node)
                retVal += 1

        return retVal