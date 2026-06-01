class Solution:

    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        nodes = {}  # nodeId : [(weight, nodeId)]

        for i in range(n):
            nodes[i+1] = []

        for t in times:
            node1 = t[0]
            node2 = t[1]
            weight = t[2]
            nodes[node1].append((weight, node2))

        minHeap = [(0, k)]
        visited = set()
        totalTime = 0

        while minHeap and len(visited) < n:
            vals = heapq.heappop(minHeap)
            curr = vals[1]
            time = vals[0]

            totalTime = max(totalTime, time)

            print(nodes)
            for child in nodes[curr]:
                newNode = child[1]
                if newNode not in visited:
                    newWeight = child[0]
                    heapq.heappush(minHeap, (time+newWeight, newNode))

            visited.add(curr)

        return totalTime if len(visited) == n else -1