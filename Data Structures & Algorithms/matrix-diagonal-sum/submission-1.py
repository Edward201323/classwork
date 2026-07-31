class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        length = len(mat)

        overlap_index = -1
        if length % 2 == 1:
            overlap_index = length // 2

        sum = 0
        for index in range(length):
            if index != overlap_index:
                sum += mat[index][index]
        
        row_index = length - 1
        col_index = 0
        while row_index >= 0:
            sum += mat[row_index][col_index]
            row_index -= 1
            col_index += 1
            
        return sum