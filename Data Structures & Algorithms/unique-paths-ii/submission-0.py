class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        bottomRow = obstacleGrid[-1]
        if bottomRow[-1] == 1:
            return 0
        prevRow = [0] * len(obstacleGrid[0])
        prevRow[-1] = 1
        
        
        for col in range(len(prevRow)-2, -1, -1):
            if bottomRow[col] == 1 or prevRow[col+1] == 0:
                prevRow[col] = 0
            else:
                prevRow[col] = prevRow[col+1]

        print(prevRow)
        for row in range(len(obstacleGrid)-2, -1, -1):
            newRow = [0] * len(obstacleGrid[0])
            newRow[-1] = prevRow[-1] if obstacleGrid[row][-1] != 1 else 0

            for col in range(len(prevRow)-2, -1, -1):
                if obstacleGrid[row][col] != 1:
                    newRow[col] = newRow[col+1] + prevRow[col]
                else:
                    newRow[col] = 0

            prevRow = newRow
            print(prevRow)

        return prevRow[0]



"""
[0,0,0],
[0,0,1],
[0,1,0]

[0,0,0]
[0,0,0]
[0,0,1]
"""