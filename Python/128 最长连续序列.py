"""
128. 最长连续序列
给定一个未排序的整数数组，找出最长连续序列的长度。

要求算法的时间复杂度为 O(n)。

示例:

输入: [100, 4, 200, 1, 3, 2]
输出: 4
解释: 最长连续序列是 [1, 2, 3, 4]。它的长度为 4。
"""

class Solution:
    def longestConsecutive(self, nums):
        if len(nums) == 0:
            return 0
        maxLen = 1
        lastNum = 10e9
        nums = list(set(nums))
        nums.sort()
        nowLen = 1
        for n in nums:
            if n - lastNum == 1:
                nowLen += 1
                maxLen = max(maxLen,nowLen)
            else:
                nowLen = 1
            lastNum = n
        return maxLen

#哈希
class Solution:
    def longestConsecutive(self, nums):
        if nums == []:
            return 0
        maxVal = max(nums)
        minVal = min(nums)
        hashSet = [0 for i in range(maxVal - minVal + 1)]
        for i in nums:
            hashSet[i - minVal] = 1
        nowLen = 0
        maxLen = 0
        for i in hashSet:
            if i == 1:
                nowLen += 1
            if i == 0:
                maxLen = max(maxLen,nowLen)
                nowLen = 0
        maxLen = max(maxLen,nowLen)
        return maxLen

#官方
class Solution:
    def longestConsecutive(self, nums):
        longest_streak = 0
        num_set = set(nums)

        for num in num_set:
            if num - 1 not in num_set:
                current_num = num
                current_streak = 1

                while current_num + 1 in num_set:
                    current_num += 1
                    current_streak += 1

                longest_streak = max(longest_streak, current_streak)

        return longest_streak

s = Solution()
print(s.longestConsecutive([0,-1]))