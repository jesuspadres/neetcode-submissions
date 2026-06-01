class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        retVal = 0
        visited = set() # Point (row, col)
        reachableHeap = []  # [pointVal, point]
        reachableSet = set()    # (row, val)

        def bfs():
            nonlocal retVal, visited, reachableHeap, reachableSet
            if not reachableHeap:
                return
            currVals = heapq.heappop(reachableHeap)
            currPoint = currVals[1]
            currRow = currPoint[0]
            currCol = currPoint[1]
            currVal = currVals[0]

            retVal = max(retVal, currVal)
            visited.add(currPoint)
        
            if (len(grid)-1, len(grid[0])-1) == currPoint:
                return

            top = (currRow-1, currCol)
            bottom = (currRow+1, currCol)
            left = (currRow, currCol-1)
            right = (currRow, currCol+1)

            if currRow - 1 >= 0 and top not in reachableSet and top not in visited:
                nextVal = grid[currRow-1][currCol]
                heapq.heappush(reachableHeap, [nextVal, top])
                reachableSet.add(top)
            if currRow + 1 < len(grid) and bottom not in reachableSet and bottom not in visited:
                nextVal = grid[currRow+1][currCol]
                heapq.heappush(reachableHeap, [nextVal, bottom])
                reachableSet.add(bottom)
            if currCol - 1 >= 0 and left not in reachableSet and left not in visited:
                nextVal = grid[currRow][currCol-1]
                heapq.heappush(reachableHeap, [nextVal, left])
                reachableSet.add(left)
            if currCol + 1 < len(grid[0]) and right not in reachableSet and right not in visited:
                nextVal = grid[currRow][currCol+1]
                heapq.heappush(reachableHeap, [nextVal, right])
                reachableSet.add(right)

            bfs()

        startPoint = (0, 0)
        reachableSet.add(startPoint)
        heapq.heappush(reachableHeap, [grid[0][0], startPoint])
        bfs()

        return retVal

        
            
