class Solution:
    def findNumberIn2DArray(self, matrix: List[List[int]], target: int) -> bool:
        # 方法1： 暴力求解
        # 代码略

        # 方法2： 利用矩阵特点，一次缩小一列或一行的取值范围
        if not matrix:
            return False
        row = 0
        col = len(matrix[0])-1

        while row < len(matrix) and col >= 0:
            if matrix[row][col] == target:
                return True
            elif matrix[row][col] > target:
                col -= 1
            else:
                row += 1
        return False
