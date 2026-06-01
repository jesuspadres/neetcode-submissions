class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        

        left = 0
        right = len(matrix)-1

        while left < right:
            for i in range(left, right):
                tmp = matrix[left][i]
                matrix[left][i] = matrix[-1-i][left]
                matrix[-1-i][left] = matrix[right][-1-i]
                matrix[right][-1-i] = matrix[i][right]
                matrix[i][right] = tmp
            left += 1
            right -= 1

        
            
[5,1,9,11],
[2,4,8,10],
[13,3,6,7],
[15,14,12,16]

[15,13,2,5],
[14,3,8,1],
[12,6,4,9],
[16,7,10,11]