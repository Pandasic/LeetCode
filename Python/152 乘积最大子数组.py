"""
152. 乘积最大子数组
给你一个整数数组 nums ，请你找出数组中乘积最大的连续子数组（该子数组中至少包含一个数字），并返回该子数组所对应的乘积。

 

示例 1:

输入: [2,3,-2,4]
输出: 6
解释: 子数组 [2,3] 有最大乘积 6。
示例 2:

输入: [-2,0,-1]
输出: 0
解释: 结果不能为 2, 因为 [-2,-1] 不是子数组。
"""
'''
    动态规划
    由于 符号有正有负还有0
    所以同时记录最大与最小值 并进行比较
'''

class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        maxArr = [0 for i in range(len(nums))]
        minArr = [0 for i in range(len(nums))]
        maxArr[0] = nums[0]
        minArr[0] = nums[0]
        for i in range(1,len(nums)):
            maxArr[i] = max(maxArr[i-1]*nums[i],minArr[i-1]*nums[i],nums[i])
            minArr[i] = min(minArr[i-1]*nums[i],maxArr[i-1]*nums[i],nums[i])
        return max(maxArr)