"""
5397. 最简分数 显示英文描述 
通过的用户数705
尝试过的用户数836
用户总通过次数708
用户总提交次数1111
题目难度Medium
给你一个整数 n ，请你返回所有 0 到 1 之间（不包括 0 和 1）满足分母小于等于  n 的 最简 分数 。分数可以以 任意 顺序返回。

 

示例 1：

输入：n = 2
输出：["1/2"]
解释："1/2" 是唯一一个分母小于等于 2 的最简分数。
示例 2：

输入：n = 3
输出：["1/2","1/3","2/3"]
示例 3：

输入：n = 4
输出：["1/2","1/3","1/4","2/3","3/4"]
解释："2/4" 不是最简分数，因为它可以化简为 "1/2" 。
示例 4：

输入：n = 1
输出：[]
"""


class Solution:
    def simplifiedFractions(self, n: int):
        res = set()
        temp = set()
        for i in range(1,n+1):
            for j in range(1,i):
                if (j/i) not in temp:
                    temp.add(j/i)
                    res.add(str(j)+"/" +str(i))
        res = list(res)
        res.sort()
        return res 

s = Solution()
for i in range(1,101):
    print(s.simplifiedFractions(i))