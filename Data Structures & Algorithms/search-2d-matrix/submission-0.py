class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        top = 0
        bottom = len(matrix)
        left = 0
        right = len(matrix[0])

        while top < bottom:
            midRow = (top+bottom)//2

            if target >= matrix[midRow][0] and target <= matrix[midRow][-1]:
                while left < right:
                    midCol = (left+right)//2

                    if matrix[midRow][midCol] == target:
                        return True
                    elif matrix[midRow][midCol] > target:
                        right = midCol
                    else:
                        left = midCol+1
                break
            elif target < matrix[midRow][0]:
                bottom = midRow
            else:
                top = midRow+1

        return False