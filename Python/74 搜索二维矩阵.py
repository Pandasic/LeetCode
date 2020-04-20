"""
74. 搜索二维矩阵
编写一个高效的算法来判断 m x n 矩阵中，是否存在一个目标值。该矩阵具有如下特性：

每行中的整数从左到右按升序排列。
每行的第一个整数大于前一行的最后一个整数。
示例 1:

输入:
matrix = [
  [1,   3,  5,  7],
  [10, 11, 16, 20],
  [23, 30, 34, 50]
]
target = 3
输出: true
示例 2:

输入:
matrix = [
  [1,   3,  5,  7],
  [10, 11, 16, 20],
  [23, 30, 34, 50]
]
target = 13
输出: false
通过次数36,054提交次数95,793
"""
#二分法
class Solution:
    def searchMatrix(self, matrix, target: int) -> bool:
        M = len(matrix)
        if M == 0 :
            return False
        N = len(matrix[0])
        if N == 0:
            return False

        row = -1
        col = -1
    
        rBegin = -1
        rEnd  = M

        #判断所在行
        while rBegin < rEnd -1:
            if target < matrix[(rBegin+rEnd)//2][0]:
                rEnd = (rBegin+rEnd)//2
            else:
                rBegin = (rBegin+rEnd)//2
        
        row = rBegin

        if row == -1:
            return False
        
        rBegin = -1
        rEnd  = N

        #判断所在行
        while rBegin < rEnd-1:
            if target < matrix[row][(rBegin+rEnd)//2]:
                rEnd = (rBegin+rEnd)//2
            elif target > matrix[row][(rBegin+rEnd)//2]:
                rBegin = (rBegin+rEnd)//2
            else:
                return True
        return False

s =Solution()
s.searchMatrix([[1]],1)