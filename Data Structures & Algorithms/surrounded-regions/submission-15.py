class Solution:
    def solve(self, board: List[List[str]]) -> None:

        def dfs(row, col):  
            board[row][col] = "V"

            if row-1 >= 0 and board[row-1][col] == "O":
                dfs(row-1, col)
            if row+1 < len(board) and board[row+1][col] == "O":
                dfs(row+1, col)
            if col-1 >= 0 and board[row][col-1] == "O":
                dfs(row, col-1)
            if col+1 < len(board[0]) and board[row][col+1] == "O":
                dfs(row, col+1)
            
        for row in range(len(board)):
            if board[row][0] == "O":
                dfs(row, 0)
            if board[row][-1] == "O":
                dfs(row, len(board[0])-1)
        for col in range(len(board[0])):
            if board[0][col] == "O":
                dfs(0, col)
            if board[-1][col] == "O":
                dfs(len(board)-1, col)

        for row in range(len(board)):
            for col in range(len(board[0])):
                if board[row][col] == "O":
                    board[row][col] = "X"
                elif board[row][col] == "V":
                    board[row][col] = "O"

    

["X","O","X","O","X","O","O","O","X","O"],
["X","O","X","X","X","X","O","O","X","X"],
["O","X","X","X","X","X","X","X","X","X"],
["O","O","X","X","X","X","X","X","X","X"],
["O","O","X","X","X","X","X","X","X","O"],
["X","X","X","X","X","X","X","X","X","O"],
["X","X","X","X","X","X","X","O","X","O"],
["X","X","O","X","X","X","X","O","O","X"],
["O","X","O","X","X","X","X","O","X","O"],
["X","X","O","X","X","X","X","O","O","O"]

["X","O","X","O","X","O","O","O","X","O"],
["X","O","O","X","X","X","O","O","O","X"],
["O","O","O","O","O","O","O","O","X","X"],
["O","O","O","O","O","O","X","O","O","X"],
["O","O","X","X","O","X","X","O","O","O"],
["X","O","O","X","X","X","X","X","X","O"],
["X","O","X","X","X","X","X","O","X","O"],
["X","X","O","X","X","X","X","O","O","X"],
["O","O","O","O","X","X","X","O","X","O"],
["X","X","O","X","X","X","X","O","O","O"]

            