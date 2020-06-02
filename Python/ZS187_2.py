"""
5401. 是否所有 1 都至少相隔 k 个元素 显示英文描述 
通过的用户数361
尝试过的用户数397
用户总通过次数361
用户总提交次数447
题目难度Medium
给你一个由若干 0 和 1 组成的数组 nums 以及整数 k。如果所有 1 都至少相隔 k 个元素，则返回 True ；否则，返回 False 。

 

示例 1：



输入：nums = [1,0,0,0,1,0,0,1], k = 2
输出：true
解释：每个 1 都至少相隔 2 个元素。
示例 2：



输入：nums = [1,0,0,1,0,1], k = 2
输出：false
解释：第二个 1 和第三个 1 之间只隔了 1 个元素。
示例 3：

输入：nums = [1,1,1,1,1], k = 0
输出：true
示例 4：

输入：nums = [0,1,0,1], k = 1
输出：true
 

提示：

1 <= nums.length <= 10^5
0 <= k <= nums.length
nums[i] 的值为 0 或 1
"""
class Solution:
    def kLengthApart(self, nums, k: int) -> bool:
        #使其指向第一个=1的元素
        begin = 0
        while begin < len(nums) and nums[begin] != 1:
            begin += 1
        if begin == len(nums):
            return True

        count = 0
        for i in range(begin+1,len(nums)):
            if nums[i] == 0:
                count += 1
            else:
                if count < k:
                    return False
                count = 0
        return True

s = Solution()
print(s.kLengthApart([1,0,0,0,1,0,0,1],2))
print(s.kLengthApart( [1,0,0,1,0,1],2))
print(s.kLengthApart([1,1,1,1,1],0))
print(s.kLengthApart([0,1,0,1],1))
print(s.kLengthApart([0,0,0],2))


        