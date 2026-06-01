class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        retVal = 0

        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == 1:
                    count = 0
                    q = set()
                    q.add((row, col))
                    while q:
                        count += 1
                        
                        p = q.pop()
                        pRow = p[0]
                        pCol = p[1]
                        print(pRow, pCol)
                        grid[pRow][pCol] = 0
                        if pRow-1 >= 0:
                            if grid[pRow-1][pCol] == 1: q.add((pRow-1, pCol))
                        if pRow+1 < len(grid):
                            if grid[pRow+1][pCol] == 1: q.add((pRow+1, pCol))
                        if pCol-1 >= 0:
                            if grid[pRow][pCol-1] == 1: q.add((pRow, pCol-1))
                        if pCol+1 < len(grid[0]):
                            if grid[pRow][pCol+1] == 1: q.add((pRow, pCol+1))
                    retVal = max(retVal, count)

        return retVal