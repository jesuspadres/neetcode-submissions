class Solution:
    def rotateTheBox(self, boxGrid: List[List[str]]) -> List[List[str]]:
        for row in range(len(boxGrid)):
            q = deque()
            for col in range(len(boxGrid[0])-1, -1, -1):
                val = boxGrid[row][col]

                if val == "*":
                    q = deque()
                elif val == ".":
                    q.append((row, col))
                elif val == "#":
                    if q:
                        point = q.popleft()
                        boxGrid[point[0]][point[1]] = "#"
                        boxGrid[row][col] = "."
                        q.append((row, col))

        retVal = []

        for col in range(len(boxGrid[0])):
            l = []
            for row in range(len(boxGrid)-1, -1, -1):
                l.append(boxGrid[row][col])
            retVal.append(l)

        return retVal
