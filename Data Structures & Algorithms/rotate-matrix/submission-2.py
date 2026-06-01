class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        
        for i in range(len(matrix)//2):
            for j in range(i, len(matrix)-i-1):
                tmp = matrix[i][j]

                matrix[i][j] = matrix[len(matrix)-j-1][i]

                matrix[len(matrix)-j-1][i] = matrix[len(matrix)-i-1][len(matrix)-j-1]

                matrix[len(matrix)-i-1][len(matrix)-j-1] = matrix[j][len(matrix)-i-1]

                matrix[j][len(matrix)-i-1] = tmp


