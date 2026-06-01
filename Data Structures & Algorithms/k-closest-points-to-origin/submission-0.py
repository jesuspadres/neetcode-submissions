class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        diffs = []
        diffMap = {}

        for p in points:
            x = p[0]
            y = p[1]

            diff = math.sqrt((x*x) + (y*y))
            heapq.heappush(diffs, diff)
            diffMap[diff] = diffMap.get(diff, [])
            diffMap[diff].append(p)

        retVal = []
        while k > 0:
            closest = heapq.heappop(diffs)
            print(diffMap)

            retVal += diffMap[closest][:k]

            k -= len(diffMap[closest])

        return retVal


