if 1:
    """
    5356. 矩阵中的幸运数 显示英文描述 
    用户通过次数0
    用户尝试次数0
    通过次数0
    提交次数0
    题目难度Easy
    给你一个 m * n 的矩阵，矩阵中的数字 各不相同 。请你按 任意 顺序返回矩阵中的所有幸运数。

    幸运数是指矩阵中满足同时下列两个条件的元素：

    在同一行的所有元素中最小
    在同一列的所有元素中最大
    

    示例 1：

    输入：matrix = [[3,7,8],[9,11,13],[15,16,17]]
    输出：[15]
    解释：15 是唯一的幸运数，因为它是其所在行中的最小值，也是所在列中的最大值。
    示例 2：

    输入：matrix = [[1,10,4,2],[9,3,8,7],[15,16,17,12]]
    输出：[12]
    解释：12 是唯一的幸运数，因为它是其所在行中的最小值，也是所在列中的最大值。
    示例 3：

    输入：matrix = [[7,8],[1,2]]
    输出：[7]
    

    提示：

    m == mat.length
    n == mat[i].length
    1 <= n, m <= 50
    1 <= matrix[i][j] <= 10^5
    矩阵中的所有元素都是不同的

    """

class Solution:
    def luckyNumbers (self, matrix):
        #行数 列数
        M = len(matrix)
        N = len(matrix[0])
        res = []
        for i in range(N):
            for j in range(M):
                now_val = matrix[j][i]
                isPass =True
                for k in range(N):
                    if matrix[j][k] < now_val:
                        isPass = False
                        break
                for k in range(M):
                    if matrix[k][i] > now_val:
                        isPass = False
                        break
                if isPass:
                    res.append(now_val)
        return res

s = Solution()
print(s.luckyNumbers([[1,10,4,2],[9,3,8,7],[15,16,17,12]]))