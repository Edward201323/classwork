class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        length = len(mat)
        sum = 0

        for i in range(length):
            sum += mat[i][i]
            sum += mat[i][length - 1 - i]
        
        if length % 2 == 1:
            sum -= mat[length // 2][length // 2]

        return sum