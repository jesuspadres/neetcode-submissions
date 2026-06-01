class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        airports = [[] for _ in range(n)]

        for flight in flights:
            a1 = flight[0]
            a2 = flight[1]
            cost = flight[2]

            airports[a1].append([a2, cost])


        retVal = float("inf")
        print(airports)

        def dfs(start, end, kVal, count):
            nonlocal retVal
            if start == end:
                retVal = min(retVal, count)
                return 
            if kVal < 0:
                return

            for flight in airports[start]:
                next = flight[0]
                cost = flight[1]
                dfs(next, end, kVal-1, count+cost)

        dfs(src, dst, k, 0)

        if retVal == float("inf"):
            return -1

        return retVal



            
