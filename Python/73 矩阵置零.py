"""
给定一个 m x n 的矩阵，如果一个元素为 0，则将其所在行和列的所有元素都设为 0。请使用原地算法。

示例 1:

输入: 
[
  [1,1,1],
  [1,0,1],
  [1,1,1]
]
输出: 
[
  [1,0,1],
  [0,0,0],
  [1,0,1]
]
示例 2:

输入: 
[
  [0,1,2,0],
  [3,4,5,2],
  [1,3,1,5]
]
输出: 
[
  [0,0,0,0],
  [0,4,5,0],
  [0,3,1,0]
]
进阶:

一个直接的解决方案是使用  O(mn) 的额外空间，但这并不是一个好的解决方案。
一个简单的改进方案是使用 O(m + n) 的额外空间，但这仍然不是最好的解决方案。
你能想出一个常数空间的解决方案吗？

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/set-matrix-zeroes
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""

class Solution:
    def setZeroes(self, matrix) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        #将每行鱼每列的第一个元素作为标识符

        #第一行是否需要置0的标志
        isFirstRowSetZero = False
        #第一行特殊处理
        for index in range(len(matrix[0])):
            if matrix[0][index] == 0:
                isFirstRowSetZero = True
        
        #找出并标识
        if len(matrix) > 1:
           for row in range(1,len(matrix)):
               for col in range(len(matrix[0])):
                    if matrix[row][col] == 0:
                        matrix[row][0] = 0
                        matrix[0][col] = 0
        
        #赋值
        for row in range(1,len(matrix)):
            if matrix[row][0] == 0:
                for col in range(1,len(matrix[0])):
                    matrix[row][col] = 0

        for col in range(len(matrix[0])):
            if matrix[0][col] == 0:
                for row in range(1,len(matrix)):
                    matrix[row][col] = 0

        if isFirstRowSetZero:
            for col in range(len(matrix[0])):
                matrix[0][col] = 0