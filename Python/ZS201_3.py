"""
5471. 和为目标值的最大数目不重叠非空子数组数目 显示英文描述 
通过的用户数298
尝试过的用户数464
用户总通过次数301
用户总提交次数632
题目难度Medium
给你一个数组 nums 和一个整数 target 。

请你返回 非空不重叠 子数组的最大数目，且每个子数组中数字和都为 target 。

 

示例 1：

输入：nums = [1,1,1,1,1], target = 2
输出：2
解释：总共有 2 个不重叠子数组（加粗数字表示） [1,1,1,1,1] ，它们的和为目标值 2 。
示例 2：

输入：nums = [-1,3,5,1,4,2,-9], target = 6
输出：2
解释：总共有 3 个子数组和为 6 。
([5,1], [4,2], [3,5,1,4,2,-9]) 但只有前 2 个是不重叠的。
示例 3：

输入：nums = [-2,6,6,3,5,4,1,2,8], target = 10
输出：3
示例 4：

输入：nums = [0,0,0], target = 0
输出：3
 

提示：

1 <= nums.length <= 10^5
-10^4 <= nums[i] <= 10^4
0 <= target <= 10^6
"""
class Solution:
    def maxNonOverlapping(self, nums, target) -> int:
        arrs = set()
        def getSubArrs(begin,itor,sum):
            if itor >= len(nums):
                return
            if nums[itor] == target:
                arrs.add((itor,itor))
            if sum + nums[itor] == target:
                arrs.add((begin,itor))
            else:
                getSubArrs(begin,itor+1,sum+nums[itor])
            getSubArrs(itor ,itor+1,nums[itor])
            
        getSubArrs(0,0,0)
        arrs = list(arrs)
        arrs.sort(key = lambda x:x[0])
        
        dp = [[0 for i in range(target) + 1] for j in range(len(arr) + 1)]
        for i in range(len(arr)):
            m = 0
            b,e = arr[i]
            for j in range(i):
                m = max(m,dp[b - 1 + 1])
            for j in range(b + 1,target + 1):
                if j <= e + 1:
                    dp[i][j] = m
                else:
                    dp[i][j] = m + 1
        return dp[len(arr) - 1][target]

s = Solution()
print(s.fun())