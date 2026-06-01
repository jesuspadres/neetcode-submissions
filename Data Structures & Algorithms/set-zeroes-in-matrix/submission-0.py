class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        for row in range(len(matrix)):
            for col in range(len(matrix[0])):
                val = matrix[row][col]

                if val != 0:
                    continue

                for r in range(len(matrix)):
                    if matrix[r][col] != 0:
                        matrix[r][col] = None

                for c in range(len(matrix[0])):
                    if matrix[row][c] != 0:
                        matrix[row][c] = None

        
        for row in range(len(matrix)):
            for col in range(len(matrix[0])):
                val = matrix[row][col]

                if val == None:
                    matrix[row][col] = 0

                    