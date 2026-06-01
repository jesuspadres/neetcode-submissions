class Solution:
    def rotateTheBox(self, boxGrid: List[List[str]]) -> List[List[str]]:

        for row in range(len(boxGrid)):
            q = deque()
            for col in range(len(boxGrid[0])-1, -1, -1):
                if boxGrid[row][col] == "*":
                    q = deque()
                elif boxGrid[row][col] == ".":
                    q.append([row, col])
                elif boxGrid[row][col] == "#" and q:
                    pair = q.popleft()
                    boxGrid[pair[0]][pair[1]] = "#"
                    boxGrid[row][col] = "."
                    q.append([row, col])

        retVal = []

        for col in range(len(boxGrid[0])):
            l = []
            for row in range(len(boxGrid)-1, -1, -1):
                l.append(boxGrid[row][col])
            retVal.append(l)

        return retVal
