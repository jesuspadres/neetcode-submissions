class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        retVal = 0

        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == "1":
                    retVal += 1
                    q = [[row, col]]
                    while q:
                        p = q.pop()
                        pRow = p[0]
                        pCol = p[1]
                        grid[pRow][pCol] = "0"
                        if pRow-1 >= 0:
                            if grid[pRow-1][pCol] == "1": q.append([pRow-1, pCol])
                        if pRow+1 < len(grid):
                            if grid[pRow+1][pCol] == "1": q.append([pRow+1, pCol])
                        if pCol-1 >= 0:
                            if grid[pRow][pCol-1] == "1": q.append([pRow, pCol-1])
                        if pCol+1 < len(grid[0]):
                            if grid[pRow][pCol+1] == "1": q.append([pRow, pCol+1])

        return retVal
                    
                    

