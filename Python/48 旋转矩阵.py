import math

import numpy as np
class Solution:
    def rotate(self, matrix) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
        #层
        for i in range(n//2):
            start = i
            end = n - i - 1
            for j in range(0,end-start):
                temp = matrix[start][start + j]
                matrix[start][start + j] = matrix[end - j][start]
                matrix[end - j][start] = matrix[end][end - j]
                matrix[end][end - j] = matrix[start + j][end]
                matrix[start + j][end] = temp

s = Solution()
s.rotate(
[
  [ 5, 1, 9,11],
  [ 2, 4, 8,10],
  [13, 3, 6, 7],
  [15,14,12,16]
])