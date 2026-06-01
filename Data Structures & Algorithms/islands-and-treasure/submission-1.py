class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        visited = set()
        s = deque()

        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == 0:
                    s.append((row, col))

        while s:
            point = s.popleft()
            if point in visited:
                continue
            row = point[0]
            col = point[1]

            visited.add(point)

            if row-1 >= 0:
                grid[row-1][col] = min(grid[row-1][col], grid[row][col]+1)
                if (row-1, col) not in visited and grid[row-1][col] != -1:
                    s.append((row-1, col))
            if col-1 >= 0:
                grid[row][col-1] = min(grid[row][col-1], grid[row][col]+1)
                if (row, col-1) not in visited and grid[row][col-1] != -1:
                    s.append((row, col-1))
            if row+1 < len(grid):
                grid[row+1][col] = min(grid[row+1][col], grid[row][col]+1)
                if (row+1, col) not in visited and grid[row+1][col] != -1:
                    s.append((row+1, col))
            if col+1 < len(grid[0]):
                grid[row][col+1] = min(grid[row][col+1], grid[row][col]+1)
                if (row, col+1) not in visited and grid[row][col+1] != -1:
                    s.append((row, col+1))
            
        