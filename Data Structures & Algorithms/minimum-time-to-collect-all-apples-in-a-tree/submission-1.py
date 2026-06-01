class Solution:
    def minTime(self, n: int, edges: List[List[int]], hasApple: List[bool]) -> int:
        graph = {}
        for i in range(n):
            graph[i] = []

        for edge in edges:
            graph[edge[0]].append(edge[1])
            graph[edge[1]].append(edge[0])

        print(graph)

        def dfs(root, parent):

            count = 0
            for node in graph[root]:
                if node != parent:
                    appDist = dfs(node, root)
                    count += appDist

            if hasApple[root] or count > 0:
                return count + 1

            return count

        return max(0, (2 * dfs(0, 0)) - 2)