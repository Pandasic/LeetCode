"""
5385. 改变一个整数能得到的最大差值 显示英文描述 
通过的用户数123
尝试过的用户数236
用户总通过次数124
用户总提交次数352
题目难度Medium
给你一个整数 num 。你可以对它进行如下步骤恰好 两次 ：

选择一个数字 x (0 <= x <= 9).
选择另一个数字 y (0 <= y <= 9) 。数字 y 可以等于 x 。
将 num 中所有出现 x 的数位都用 y 替换。
得到的新的整数 不能 有前导 0 ，得到的新整数也 不能 是 0 。
令两次对 num 的操作得到的结果分别为 a 和 b 。

请你返回 a 和 b 的 最大差值 。

 

示例 1：

输入：num = 555
输出：888
解释：第一次选择 x = 5 且 y = 9 ，并把得到的新数字保存在 a 中。
第二次选择 x = 5 且 y = 1 ，并把得到的新数字保存在 b 中。
现在，我们有 a = 999 和 b = 111 ，最大差值为 888
示例 2：

输入：num = 9
输出：8
解释：第一次选择 x = 9 且 y = 9 ，并把得到的新数字保存在 a 中。
第二次选择 x = 9 且 y = 1 ，并把得到的新数字保存在 b 中。
现在，我们有 a = 9 和 b = 1 ，最大差值为 8
示例 3：

输入：num = 123456
输出：820000
示例 4：

输入：num = 10000
输出：80000
示例 5：

输入：num = 9288
输出：8700
 

提示：

1 <= num <= 10^8
"""

#暴力
class Solution:
    def maxDiff(self, num: int) -> int:
        def getParts(num):
            res = list(set(list(str(num))))
            for i in range(len(res)):
                res[i] = int(res[i])
            return res
        def getPos(num,index = 0):
            return int(str(num)[index])
        def numReplace(num,r,p):
            n = str(num)
            n = n.replace(str(r),str(p))
            return int(n)

        def isStartWithZero(orin,now):
            if len(str(orin)) == len(str(orin)):
                return True
            else:
                return False
        #max
        maxVal = 0
        for i in range(9,0,-1):
            p = getParts(num)
            for v in p:
                maxVal = max(maxVal,numReplace(num,v,i))

        minVal = 10e9
        for i in range(0,9):
            p = getParts(num)
            s = getPos(num)
            for v in p:
                if i == 0 and v == s:
                    continue
                minVal = min(minVal,numReplace(num,v,i))

        return maxVal - minVal


s = Solution()
print(s.maxDiff(123456789))