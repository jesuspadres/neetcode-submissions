class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        q = deque() # [row, col, time]
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == 1:
                    alone = True
                    if row-1 >= 0:
                        alone = alone and grid[row-1][col] == 0
                    if col-1 >= 0:
                        alone = alone and grid[row][col-1] == 0
                    if row+1 < len(grid):
                        alone = alone and grid[row+1][col] == 0
                    if col+1 < len(grid[0]):
                        alone = alone and grid[row][col+1] == 0
                    if alone:
                        return -1
                elif grid[row][col] == 2:
                    q.append([row, col, 0])

        retVal = 0
        while q:
            vals = q.popleft()
            row = vals[0]
            col = vals[1]
            t = vals[2]
            retVal = max(retVal, t)

            if row-1 >= 0:
                if grid[row-1][col] == 1:
                    q.append([row-1, col, t+1])
                    grid[row-1][col] = 2
            if col-1 >= 0:
                if grid[row][col-1] == 1:
                    q.append([row, col-1, t+1])
                    grid[row][col-1] = 2
            if row+1 < len(grid):
                if grid[row+1][col] == 1:
                    q.append([row+1, col, t+1])
                    grid[row+1][col] = 2
            if col+1 < len(grid[0]):
                if grid[row][col+1] == 1:
                    q.append([row, col+1, t+1])
                    grid[row][col+1] = 2

        return retVal






[[2,0,1,1,1,1,1,1,1,1]
,[1,0,1,0,0,0,0,0,0,1]
,[1,0,1,0,1,1,1,1,0,1]
,[1,0,1,0,1,0,0,1,0,1]
,[1,0,1,0,1,0,0,1,0,1]
,[1,0,1,0,1,1,0,1,0,1]
,[1,0,1,0,0,0,0,1,0,1]
,[1,0,1,1,1,1,1,1,0,1]
,[1,0,0,0,0,0,0,0,0,1]
,[1,1,1,1,1,1,1,1,1,1]]
