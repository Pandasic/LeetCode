"""
5456. 在区间范围内统计奇数数目 显示英文描述 
通过的用户数0
尝试过的用户数0
用户总通过次数0
用户总提交次数0
题目难度Easy
给你两个非负整数 low 和 high 。请你返回 low 和 high 之间（包括二者）奇数的数目。

 

示例 1：

输入：low = 3, high = 7
输出：3
解释：3 到 7 之间奇数数字为 [3,5,7] 。
示例 2：

输入：low = 8, high = 10
输出：1
解释：8 到 10 之间奇数数字为 [9] 。
 

提示：

0 <= low <= high <= 10^9
"""
class Solution:
    def countOdds(self, low: int, high: int) -> int:
        offset = high - low
        if low%2 == 1:
            res = 1 + offset//2
        else:
            res = offset//2 + offset %2
        return res
            
s = Solution()
print(s.fun())