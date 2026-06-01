class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        retVal = 1

        cache = {}

        def dfs(row, col):
            if (row, col) in cache:
                return cache[(row, col)]

            thisVal = matrix[row][col]
            maxPath = 1

            if row-1 >= 0 and matrix[row-1][col] > thisVal:
                maxPath = max(maxPath, dfs(row-1, col)+1)
            if col-1 >= 0 and matrix[row][col-1] > thisVal:
                maxPath = max(maxPath, dfs(row, col-1)+1)
            if row+1 < len(matrix) and matrix[row+1][col] > thisVal:
                maxPath = max(maxPath, dfs(row+1, col)+1)
            if col+1 < len(matrix[0]) and matrix[row][col+1] > thisVal:
                maxPath = max(maxPath, dfs(row, col+1)+1)


            cache[(row, col)] = maxPath

            return maxPath

        for row in range(len(matrix)):
            for col in range(len(matrix[0])):
                retVal = max(retVal, dfs(row, col))

        return retVal

            