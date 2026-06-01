class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        flightMap = {}
        tickets.sort()

        for ticket in tickets:
            c1 = ticket[0]
            c2 = ticket[1]

            if c1 not in flightMap:
                flightMap[c1] = []
            flightMap[c1].append(c2)


        print(flightMap)

        flightPath = []

        def dfs(path):
            nonlocal flightPath
            if len(path) == len(tickets)+1:
                print(path)
                flightPath += path
                return True
            city = path[-1]

            temp = flightMap.get(city, [])
            for i, nextCity in enumerate(temp):
                flightMap[city].pop(i)
                if dfs(path+[nextCity]):
                    return True
                flightMap[city].insert(i, nextCity)

        dfs(["JFK"])

        return flightPath

