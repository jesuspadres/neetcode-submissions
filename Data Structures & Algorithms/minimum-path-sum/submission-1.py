class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        rowLen = len(grid[-1])
        for col in range(rowLen-2, -1, -1):
            grid[-1][col] += grid[-1][col+1]

        for row in range(len(grid)-2, -1, -1):
            grid[row][-1] += grid[row+1][-1]

            for col in range(rowLen-2, -1, -1):
                minVal = min(grid[row+1][col], grid[row][col+1])
                grid[row][col] += minVal

        return grid[0][0]
                

"""
[1,2,0],
[5,4,2],
[1,1,3]


[8,7,5],
[10,8,5],
[5,4,3]
"""