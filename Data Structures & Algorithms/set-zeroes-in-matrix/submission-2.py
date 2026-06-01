class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        ROWS, COLS = len(matrix), len(matrix[0])    # Optimal
        rowZero = False

        for r in range(ROWS):
            for c in range(COLS):
                if matrix[r][c] == 0:
                    matrix[0][c] = 0
                    if r > 0:
                        matrix[r][0] = 0
                    else:
                        rowZero = True

        for r in range(1, ROWS):
            for c in range(1, COLS):
                if matrix[0][c] == 0 or matrix[r][0] == 0:
                    matrix[r][c] = 0

        if matrix[0][0] == 0:
            for r in range(ROWS):
                matrix[r][0] = 0

        if rowZero:
            for c in range(COLS):
                matrix[0][c] = 0
        return

# My solution

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

