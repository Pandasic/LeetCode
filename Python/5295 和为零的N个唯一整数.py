"""
5295. 和为零的N个唯一整数 显示英文描述 
题目难度Easy
给你一个整数 n，请你返回 任意 一个由 n 个各不相同的 整数 组成的数组，并且这 n 个数相加和为 0 。

 

示例 1：

输入：n = 5
输出：[-7,-1,1,3,4]
解释：这些数组也是正确的 [-5,-1,1,2,3]，[-3,-1,2,-2,4]。
示例 2：

输入：n = 3
输出：[-1,0,1]
示例 3：

输入：n = 1
输出：[0]
 

提示：

1 <= n <= 1000

"""
class Solution:
    def sumZero(self, n: int):
        if n%2 == 1:
            res = [-i for i in range(1,n//2 + 1)] + [0] + [i for i in range(1,n//2 + 1)]
        else:
            res = [-i for i in range(1,n//2 + 1)] + [i for i in range(1,n//2 + 1)]
        return res

s = Solution()
print(s.sumZero(9))
print(s.sumZero(1))