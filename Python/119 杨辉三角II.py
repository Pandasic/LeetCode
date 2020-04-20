"""
119. 杨辉三角 II
给定一个非负索引 k，其中 k ≤ 33，返回杨辉三角的第 k 行。



在杨辉三角中，每个数是它左上方和右上方的数的和。

示例:

输入: 3
输出: [1,3,3,1]
进阶：

你可以优化你的算法到 O(k) 空间复杂度吗？

通过次数47,017提交次数77,440
在真实的面试中遇到过这道题？
"""
class Solution:
    def getRow(self, rowIndex: int):
        res = []
        numRows = rowIndex +1
        if numRows == 1:
            return [1]
        elif numRows == 2:
            return [1,1]
        else:
            res = [[1],[1,1]]
            for i in range(3,numRows + 1):
                line = [1]
                for j in range(1,i-1):
                    line.append(res[i-2][j-1] +res[i-2][j])
                line.append(1)
                res.append(line)
        return res[-1]

/*
 * 获取杨辉三角的指定行
 * 直接使用组合公式C(n,i) = n!/(i!*(n-i)!)
 * 则第(i+1)项是第i项的倍数=(n-i)/(i+1);
 */