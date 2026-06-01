class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        def getNeighbors(point):
            neighbors = []
            left = (point[0], point[1]-1)
            right = (point[0], point[1]+1)
            up = (point[0]-1, point[1])
            down = (point[0]+1, point[1])

            if isValid(left): neighbors.append(left) 
            if isValid(right): neighbors.append(right) 
            if isValid(up): neighbors.append(up) 
            if isValid(down): neighbors.append(down) 

            return neighbors

        def isValid(point):
            row = point[0]
            col = point[1]

            if row < len(board) and row >= 0 and col >= 0 and col < len(board[0]):
                return True

            return False

        def search(currPoint, currWord, visited):
            row = currPoint[0]
            col = currPoint[1]
            
            if currWord == "" or (currWord == board[row][col] and currPoint not in visited):
                return True
            
            if currWord[0] != board[row][col]:
                return False
            print(board[row][col], currWord)

            retVal = False
            neighbors = getNeighbors(currPoint)
            for n in neighbors:
                if n not in visited:
                    visited.add(currPoint)
                    retVal = retVal or search(n, currWord[1:], visited)
                    visited.remove(currPoint)

            return retVal

        for row in range(len(board)):
            for col in range(len(board[0])):
                r = search((row, col), word, set())
                if r:
                    return True

        return False


            


        