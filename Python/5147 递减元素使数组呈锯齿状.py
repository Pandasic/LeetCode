"""
5147. 递减元素使数组呈锯齿状  显示英文描述  
用户通过次数 0
用户尝试次数 0
通过次数 0
提交次数 0
题目难度 Easy
给你一个整数数组 nums，每次 操作 会从中选择一个元素并 将该元素的值减少 1。

如果符合下列情况之一，则数组 A 就是 锯齿数组：

每个偶数索引对应的元素都大于相邻的元素，即 A[0] > A[1] < A[2] > A[3] < A[4] > ...
或者，每个奇数索引对应的元素都小于相邻的元素，即 A[0] < A[1] > A[2] < A[3] > A[4] < ...
返回将数组 nums 转换为锯齿数组所需的最小操作次数。

示例 1：

输入：nums = [1,2,3]
输出：2
解释：我们可以把 2 递减到 0，或把 3 递减到 1。

示例 2：

输入：nums = [9,6,1,6,2]
输出：4
"""

class Solution:
    def movesToMakeZigzag(self, nums):
        res = 100000
        length = len(nums)
        #偶数情况
        if length % 2 == 1:
            temp = 0
            for i in range(1,length,2):
                if nums[i] >= min(nums[i-1],nums[i+1]):
                    temp +=  nums[i] - min(nums[i-1],nums[i+1]) + 1
            res = min(res,temp)
        else:
            temp = 0
            for i in range(1,length - 1,2):
                if nums[i] >= min(nums[i-1],nums[i+1]):
                    temp += -min(nums[i-1],nums[i+1]) + nums[i] + 1
            if nums[length - 2] <= nums[length - 1]:
                temp +=  nums[length - 1] - nums[length - 2] + 1
            res = min(res,temp)

        #奇数情况
        if length % 2 == 1:
            temp = 0
            if nums[0] > nums[1]:
                temp += nums[0] - nums[1] + 1
            for i in range(2,length - 2,2):
                if nums[i] >= min(nums[i-1],nums[i+1]):
                    temp +=  nums[i] - min(nums[i-1],nums[i+1]) + 1
            if nums[length - 2] <= nums[length - 1]:
                temp +=  nums[length - 1] - nums[length - 2] + 1
            res = min(res,temp)
        else:
            temp = 0
            if nums[0] > nums[1]:
                temp += nums[0] - nums[1] + 1
            for i in range(1,length - 2,2):
                if nums[i] >= min(nums[i-1],nums[i+1]):
                    temp +=  -min(nums[i-1],nums[i+1]) + nums[i] + 1
            res = min(res,temp)
        return res

s = Solution()
print(s.movesToMakeZigzag([2,7,10,9,8,9]))
