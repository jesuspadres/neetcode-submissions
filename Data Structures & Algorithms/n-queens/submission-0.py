class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        board = [["." for _ in range(n)] for _ in range(n)]
        columns = ["_" for _ in range(n)]

        retList = []


        def validPos(row, col):
            if columns[col] == "Q":
                return False

            tRow = row
            tCol = col
            while tRow >= 0 and tCol >= 0:
                if board[tRow][tCol] == "Q":
                    return False
                tRow -= 1
                tCol -= 1
            tRow = row
            tCol = col
            while tRow < n and tCol >= 0:
                if board[tRow][tCol] == "Q":
                    return False
                tRow += 1
                tCol -= 1
            tRow = row
            tCol = col
            while tRow < n and tCol < n:
                if board[tRow][tCol] == "Q":
                    return False
                tRow += 1
                tCol += 1
            tRow = row
            tCol = col
            while tRow >= 0 and tCol < n:
                if board[tRow][tCol] == "Q":
                    return False
                tRow -= 1
                tCol += 1
            return True

        def addValidBoard():
            bList = []

            for row in board:
                r = ""
                for spot in row:
                    r += spot
                bList.append(r)

            retList.append(bList)

        def placeQ(qIdx):
            if qIdx >= n:
                addValidBoard()
            
            for col in range(n):
                if validPos(qIdx, col):
                    board[qIdx][col] = "Q"
                    columns[col] = "Q"
                    placeQ(qIdx+1)
                    board[qIdx][col] = "."
                    columns[col] = "."

        placeQ(0)
        return retList



        










            
