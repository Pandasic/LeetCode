"""
给定一个由整数组成的非空数组所表示的非负整数，在该数的基础上加一。

最高位数字存放在数组的首位， 数组中每个元素只存储单个数字。

你可以假设除了整数 0 之外，这个整数不会以零开头。

示例 1:

输入: [1,2,3]
输出: [1,2,4]
解释: 输入数组表示数字 123。
示例 2:

输入: [4,3,2,1]
输出: [4,3,2,2]
解释: 输入数组表示数字 4321。
"""
class Solution:
    def plusOne(self, digits):
        if len(digits) == 0:
            return digits
        itor = -1
        #一直进位到达最大位
        while abs(itor) <= len(digits):
            digits[itor] += 1
            if digits[itor] >= 10:
                digits[itor] %= 10
                itor -= 1
            else:
                break
        else:
            return [1] + digits
        return digits

s = Solution()
print(s.plusOne([1,2,3,4]))
print(s.plusOne([9,9,9,9]))
print(s.plusOne([9]))
