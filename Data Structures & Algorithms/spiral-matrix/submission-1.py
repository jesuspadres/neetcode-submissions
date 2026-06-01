class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        retList = []
        
        for i in range((min(len(matrix), len(matrix[0]))+1) // 2):
            left = top = i
            right = len(matrix[0]) - i
            bottom = len(matrix) - i

            for col in range(left, right):
                retList.append(matrix[top][col])

            for row in range(top+1, bottom):
                retList.append(matrix[row][right-1])

            if top != bottom-1 and left != right-1:
                for col in range(right-2, left-1, -1):
                    retList.append(matrix[bottom-1][col])

                for row in range(bottom-2, top, -1):
                    retList.append(matrix[row][left])

        return retList