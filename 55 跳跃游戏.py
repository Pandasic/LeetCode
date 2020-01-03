"""
55. 跳跃游戏
给定一个非负整数数组，你最初位于数组的第一个位置。

数组中的每个元素代表你在该位置可以跳跃的最大长度。

判断你是否能够到达最后一个位置。

示例 1:

输入: [2,3,1,1,4]
输出: true
解释: 从位置 0 到 1 跳 1 步, 然后跳 3 步到达最后一个位置。
示例 2:

输入: [3,2,1,0,4]
输出: false
解释: 无论怎样，你总会到达索引为 3 的位置。但该位置的最大跳跃长度是 0 ， 所以你永远不可能到达最后一个位置

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/jump-game
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""

'''
回溯法 超时 = =
class Solution:
    def __init__(self):
        self.dp = []

    def canJump(self, nums):
        if len(nums)<= 1:
            return True
        self.dp = [None] * len(nums)
        return self.canJumpToIndex(nums,len(nums)-1)

    def canJumpToIndex(self, nums,index):
        if self.dp[index] == True:
            return True
        if self.dp[index] == False:
            return False
        res = []
        for i in range(index):
            if nums[i] + i >= index:
                res.append(i)
                if i == 0:
                    self.dp[i] = True
                    return True
        print(res)
        for r in res:
            if self.canJumpToIndex(nums,r):
                return True
        self.dp[index] = False
        return False
'''

#LeetCode 官方给的贪心算法  尽可能到达较远的地方  - - 
class Solution:
    def canJump(self, nums):
        m = 0
        for i in range(len(nums)):
            m = max(i + nums[i], m)
            if (max <= i ):
                return False
            return True