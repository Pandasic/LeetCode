"""
5423. 找两个和为目标值且不重叠的子数组 显示英文描述 
通过的用户数192
尝试过的用户数634
用户总通过次数193
用户总提交次数1322
题目难度Medium
给你一个整数数组 arr 和一个整数值 target 。

请你在 arr 中找 两个互不重叠的子数组 且它们的和都等于 target 。可能会有多种方案，请你返回满足要求的两个子数组长度和的 最小值 。

请返回满足要求的最小长度和，如果无法找到这样的两个子数组，请返回 -1 。

 

示例 1：

输入：arr = [3,2,2,4,3], target = 3
输出：2
解释：只有两个子数组和为 3 （[3] 和 [3]）。它们的长度和为 2 。
示例 2：

输入：arr = [7,3,4,7], target = 7
输出：2
解释：尽管我们有 3 个互不重叠的子数组和为 7 （[7], [3,4] 和 [7]），但我们会选择第一个和第三个子数组，因为它们的长度和 2 是最小值。
示例 3：

输入：arr = [4,3,2,6,2,3,4], target = 6
输出：-1
解释：我们只有一个和为 6 的子数组。
示例 4：

输入：arr = [5,5,4,4,5], target = 3
输出：-1
解释：我们无法找到和为 3 的子数组。
示例 5：

输入：arr = [3,1,1,1,5,1,2,1], target = 3
输出：3
解释：注意子数组 [1,2] 和 [2,1] 不能成为一个方案因为它们重叠了。
 

提示：

1 <= arr.length <= 10^5
1 <= arr[i] <= 1000
1 <= target <= 10^8
"""

class Solution:
    def minSumOfLengths(self, arr, target):
        dp = [-1 for i in range(len(arr))]

        for i in range(len(arr)):
            nowSum = 0
            index = i
            while index<len(arr) and nowSum < target:
                nowSum += arr[index]
                if nowSum == target:
                    dp[i] = index
                    print(i,index)
                    break
                index += 1
        print(dp)
        res = []
        for i in range(len(dp)):
            if dp[i] != -1:
                res.append((i,dp[i]))
        if len(res) < 2:
            return -1
        res.sort(key = lambda x:x[1] - x[0])
        print(res)
        #去重
        dp =  [False for i in range(len(arr))]
        newRes = []
        for b,e in res:
            isUsed = False
            for i in range(b,e+1):
                isUsed |= dp[i]
            if not isUsed:
                for i in range(b,e+1):
                    dp[i] = True
                newRes.append((b,e))
        if len(newRes) < 2:
            return -1
        print(newRes)
        return newRes[0][1] - newRes[0][0] + newRes[1][1]- newRes[1][0] + 2

s = Solution()
#s.minSumOfLengths([3,2,2,4,3],3)
#s.minSumOfLengths([7,3,4,7],7)
print(s.minSumOfLengths( [3,1,1,1,5,1,2,1],3))