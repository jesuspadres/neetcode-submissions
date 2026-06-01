class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        retVal = 0
        visited = set()
        pointDist = [float('inf') for _ in points]

        def getDist(p1, p2):
            x1 = p1[0]
            x2 = p2[0]
            y1 = p1[1]
            y2 = p2[1]

            return abs(x1 - x2) + abs(y1 - y2)

        def bfs(currPoint, idx):
            nonlocal retVal, visited, points, pointDist
            if len(visited) == len(points):
                return
            visited.add(idx)
            retVal += pointDist[idx]
            print(visited)

            nextPoint = None
            for i, point in enumerate(points):
                if i in visited:
                    continue
                thisDist = getDist(currPoint, point)
                pointDist[i] = min(pointDist[i], thisDist)

                if not nextPoint or pointDist[nextPoint] > pointDist[i]:
                    nextPoint = i

            if nextPoint:
                bfs(points[nextPoint], nextPoint)

        
        
        pointDist[0] = 0
        bfs(points[0], 0)

        return retVal