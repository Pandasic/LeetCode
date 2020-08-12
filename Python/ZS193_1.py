"""
5436. 一维数组的动态和 显示英文描述 
通过的用户数2289
尝试过的用户数2298
用户总通过次数2310
用户总提交次数2371
题目难度Easy
给你一个数组 nums 。数组「动态和」的计算公式为：runningSum[i] = sum(nums[0]…nums[i]) 。

请返回 nums 的动态和。

 

示例 1：

输入：nums = [1,2,3,4]
输出：[1,3,6,10]
解释：动态和计算过程为 [1, 1+2, 1+2+3, 1+2+3+4] 。
示例 2：

输入：nums = [1,1,1,1,1]
输出：[1,2,3,4,5]
解释：动态和计算过程为 [1, 1+1, 1+1+1, 1+1+1+1, 1+1+1+1+1] 。
示例 3：

输入：nums = [3,1,2,10,1]
输出：[3,4,6,16,17]
 

提示：

1 <= nums.length <= 1000
-10^6 <= nums[i] <= 10^6

"""

class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        s = 0
        for i in range(len(nums)):
            nums[i] += s
            s = nums[i]
        return nums