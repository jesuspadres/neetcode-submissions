class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for row in board:
            s = set()
            for col in row:
                if col in s and col != ".":
                    return False
                s.add(col)

        for i in range(9):
            s = set()
            for row in board:
                if row[i] in s and row[i] != ".":
                    return False
                s.add(row[i])

        return self.validSudokuSquare(board, 0, 0) and self.validSudokuSquare(board, 0, 3) and self.validSudokuSquare(board, 0, 6) and self.validSudokuSquare(board, 3, 0) and self.validSudokuSquare(board, 3, 3) and self.validSudokuSquare(board, 3, 6) and self.validSudokuSquare(board, 6, 0) and self.validSudokuSquare(board, 6, 3) and self.validSudokuSquare(board, 6, 6)

    def validSudokuSquare(self, board, rowStart, colStart):
        s = set()
        for row in range(rowStart, rowStart + 3):
            for col in range(colStart, colStart + 3):
                if board[row][col] in s and board[row][col] != ".":
                    return False
                s.add(board[row][col])

        return True