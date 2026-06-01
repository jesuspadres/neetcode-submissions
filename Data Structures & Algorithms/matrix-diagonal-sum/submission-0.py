class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        sums = 0

        col1 = 0
        col2 = len(mat[0])-1

        for row in mat:
            sums += row[col1] + row[col2]

            col1 += 1
            col2 -= 1

        if len(mat) % 2 == 1:
            x = len(mat) // 2

            sums -= mat[x][x]

        return sums