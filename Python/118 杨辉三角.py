"""
118. 杨辉三角
给定一个非负整数 numRows，生成杨辉三角的前 numRows 行。



在杨辉三角中，每个数是它左上方和右上方的数的和。

示例:

输入: 5
输出:
[
     [1],
    [1,1],
   [1,2,1],
  [1,3,3,1],
 [1,4,6,4,1]
]
通过次数70,888提交次数107,157
在真实的面试中遇到过这道题？

是
"""
class Solution:
    def generate(self, numRows):
        res = []
        if numRows == 1:
            return [[1]]
        elif numRows == 2:
            return [[1],[1,1]]
        else:
            res = [[1],[1,1]]
            for i in range(3,numRows + 1):
                line = [1]
                for j in range(1,i-1):
                    line.append(res[i-2][j-1] +res[i-2][j])
                line.append(1)
                res.append(line)
        return res

s = Solution()
print(s.generate(5))