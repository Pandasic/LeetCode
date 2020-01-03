"""
54. 螺旋矩阵
给定一个包含 m x n 个元素的矩阵（m 行, n 列），请按照顺时针螺旋顺序，返回矩阵中的所有元素。

示例 1:

输入:
[
 [ 1, 2, 3 ],
 [ 4, 5, 6 ],
 [ 7, 8, 9 ]
]
输出: [1,2,3,6,9,8,7,4,5]
示例 2:

输入:
[
  [1, 2, 3, 4],
  [5, 6, 7, 8],
  [9,10,11,12]
]
输出: [1,2,3,4,8,12,11,10,9,5,6,7]

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/spiral-matrix
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""

class Solution:
    def spiralOrder(self, matrix):
        end_m = len(matrix)
        end_n = len(matrix[0])
        begin_m = 0
        begin_n = 0
        arryDirect = [(1,0),(0,1),(-1,0),(0,-1)]
        nowDirect = 0
        res = []
        count = end_m * end_n
        now_x = 0
        now_y = 0
        while(count > 0):
            res += [matrix[now_y][now_x]]
            now_x += arryDirect[nowDirect][0]
            now_y += arryDirect[nowDirect][1]
            count -= 1
            print(count)
            if nowDirect == 0 and now_x == end_n:
                nowDirect += 1
                now_x -= 1
                now_y += 1
                end_n -= 1

            if nowDirect == 1 and now_y == end_m:
                nowDirect += 1
                now_x -= 1
                now_y -= 1
                end_m -= 1 
            
            if nowDirect == 2 and now_x == begin_m - 1:
                nowDirect += 1
                now_x += 1
                now_y -= 1
                begin_m += 1

            if nowDirect == 3 and now_y == begin_n:
                nowDirect = 0
                now_x += 1
                now_y += 1
                begin_n += 1
            print(res)
        return res

s =  Solution()
s.spiralOrder([
  [1, 2, 3, 4],
  [5, 6, 7, 8],
  [9,10,11,12]
])