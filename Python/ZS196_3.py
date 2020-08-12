"""
5454. 统计全 1 子矩形 显示英文描述 
通过的用户数495
尝试过的用户数805
用户总通过次数498
用户总提交次数1086
题目难度Medium
给你一个只包含 0 和 1 的 rows * columns 矩阵 mat ，请你返回有多少个 子矩形 的元素全部都是 1 。

 

示例 1：

输入：mat = [[1,0,1],
            [1,1,0],
            [1,1,0]]
输出：13
解释：
有 6 个 1x1 的矩形。
有 2 个 1x2 的矩形。
有 3 个 2x1 的矩形。
有 1 个 2x2 的矩形。
有 1 个 3x1 的矩形。
矩形数目总共 = 6 + 2 + 3 + 1 + 1 = 13 。
示例 2：

输入：mat = [[0,1,1,0],
            [0,1,1,1],
            [1,1,1,0]]
输出：24
解释：
有 8 个 1x1 的子矩形。
有 5 个 1x2 的子矩形。
有 2 个 1x3 的子矩形。
有 4 个 2x1 的子矩形。
有 2 个 2x2 的子矩形。
有 2 个 3x1 的子矩形。
有 1 个 3x2 的子矩形。
矩形数目总共 = 8 + 5 + 2 + 4 + 2 + 2 + 1 = 24 。
示例 3：

输入：mat = [[1,1,1,1,1,1]]
输出：21
示例 4：

输入：mat = [[1,0,1],[0,1,0],[1,0,1]]
输出：5
 

提示：

1 <= rows <= 150
1 <= columns <= 150
0 <= mat[i][j] <= 1
"""
#赛后偷偷看别人的 QAQ
class Solution:
    def numSubmat(self, mat: List[List[int]]) -> int:
        m, n = len(mat), len(mat[0])
        prefix = [[0] * (n + 1) for i in range(m + 1)]
        
        for i in range(1, m+1):
            for j in range(1, n+1):
                prefix[i][j] = prefix[i-1][j] + prefix[i][j-1] - prefix[i-1][j-1] + mat[i-1][j-1]
        
        ans = 0
        for i in range(m):
            for j in range(n):
                for k in range(m - i):
                    for l in range(n - j):
                        if prefix[i+k+1][j+l+1] - prefix[i][j+l+1] - prefix[i+k+1][j] + prefix[i][j] == (k + 1) * (l + 1):
                            ans += 1
                        else:
                            break
        return ans


s = Solution()
print(s.numSubmat([[0,0,0],[0,0,0],[0,1,1],[1,1,0],[0,1,1]]))
