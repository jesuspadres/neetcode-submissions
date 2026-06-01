class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        for i, t in enumerate(tasks):
            t.append(i)
        
        tasks.sort(key=lambda t: t[0])

        retList = []
        i = 0
        time = tasks[0][0]
        heap = []

        while len(retList) < len(tasks):
            while i < len(tasks) and tasks[i][0] <= time:
                heapq.heappush(heap, (tasks[i][1], tasks[i][2]))
                i += 1

            if heap:
                x = heapq.heappop(heap)
                retList.append(x[1])
                time += x[0]
            else:
                time = tasks[i][0]

        return retList
