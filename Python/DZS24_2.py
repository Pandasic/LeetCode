"""
5373. 和为 K 的最少斐波那契数字数目 显示英文描述 
通过的用户数48
尝试过的用户数54
用户总通过次数48
用户总提交次数55
题目难度Medium
给你数字 k ，请你返回和为 k 的斐波那契数字的最少数目，其中，每个斐波那契数字都可以被使用多次。

斐波那契数字定义为：

F1 = 1
F2 = 1
Fn = Fn-1 + Fn-2 ， 其中 n > 2 。
数据保证对于给定的 k ，一定能找到可行解。

 

示例 1：

输入：k = 7
输出：2 
解释：斐波那契数字为：1，1，2，3，5，8，13，……
对于 k = 7 ，我们可以得到 2 + 5 = 7 。
示例 2：

输入：k = 10
输出：2 
解释：对于 k = 10 ，我们可以得到 2 + 8 = 10 。
示例 3：

输入：k = 19
输出：3 
解释：对于 k = 19 ，我们可以得到 1 + 5 + 13 = 19 。
 

提示：

1 <= k <= 10^9
"""

class Solution:
    def findMinFibonacciNumbers(self, k: int) -> int:
        if k == 1:
            return 1
        fibonacci = [1,1]
        nowNum = 2
        while nowNum <= k:
            nowNum = fibonacci[-1] + fibonacci[-2]
            fibonacci.append(nowNum)
        def getPartsCount(v):
            if v == 0:
                return 0
            for n in range(len(fibonacci)):
                if fibonacci[n] > v:
                    return getPartsCount(v - fibonacci[n - 1])+1
        return getPartsCount(k)

s = Solution()
print(s.findMinFibonacciNumbers(1))
