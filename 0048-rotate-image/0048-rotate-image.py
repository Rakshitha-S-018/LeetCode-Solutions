class Solution:
    def rotate(self, matrix):
        n = len(matrix) # coz n*n matrix

        result = [[0] * n for _ in range(n)]

        for i in range(n):
            for j in range(n):
                result[j][(n - 1) - i] = matrix[i][j]
        matrix[:] = result #imp
        