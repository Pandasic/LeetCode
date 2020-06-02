"""
137. 只出现一次的数字 II
给定一个非空整数数组，除了某个元素只出现一次以外，其余每个元素均出现了三次。找出那个只出现了一次的元素。

说明：

你的算法应该具有线性时间复杂度。 你可以不使用额外空间来实现吗？

示例 1:

输入: [2,2,3,2]
输出: 3
示例 2:

输入: [0,1,0,1,0,1,99]
输出: 99
通过次数26,213提交次数39,373
"""

class mySolution:
    def singleNumber(self, nums) -> int:
        if len(nums) == 1:
            return nums[0]
        nums.sort()
        lastNum = nums[0]
        count = 1
        for i in nums[1:]:
            if i != lastNum:
                if count == 1:
                    return lastNum
                else:
                    count = 0
            count += 1
            lastNum = i
        else:
            return nums[-1]

#电路的状态
class Solution:
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        a, b = 0, 0
        for num in nums:
            b = ~a & (b ^ num)
            a = ~b & (a ^ num)
        return b

s = Solution()
s.singleNumber([17,12,5,-6,12,4,17,-5,2,-3,2,4,5,16,-3,-4,15,15,-4,-5,-6])