"""
5394. 对角线遍历 II 显示英文描述 
通过的用户数215
尝试过的用户数454
用户总通过次数215
用户总提交次数697
题目难度Medium
给你一个列表 nums ，里面每一个元素都是一个整数列表。请你依照下面各图的规则，按顺序返回 nums 中对角线上的整数。

 

示例 1：



输入：nums = [[1,2,3],[4,5,6],[7,8,9]]
输出：[1,4,2,7,5,3,8,6,9]
示例 2：



输入：nums = [[1,2,3,4,5],[6,7],[8],[9,10,11],[12,13,14,15,16]]
输出：[1,6,2,8,7,3,9,4,12,10,5,13,11,14,15,16]
示例 3：

输入：nums = [[1,2,3],[4],[5,6,7],[8],[9,10,11]]
输出：[1,4,2,5,3,8,6,9,7,10,11]
示例 4：

输入：nums = [[1,2,3,4,5,6]]
输出：[1,2,3,4,5,6]
 

提示：

1 <= nums.length <= 10^5
1 <= nums[i].length <= 10^5
1 <= nums[i][j] <= 10^9
nums 中最多有 10^5 个数字。
"""
#坐标求和入字典  然后反向输出
class Solution:
    def findDiagonalOrder(self, nums):
        temp = {}
        for y in range(len(nums)):
            for x in range(len(nums[y])):
                if x+y not in temp.keys():
                    temp[x+y] = []
                temp[x+y].append(nums[y][x])
        res = []
        vals = list(temp.keys())
        vals.sort()
        for i in vals:
            temp[i].reverse()
            res += temp[i]
        return res

s = Solution()
#print(s.findDiagonalOrder([[1,2,3],[4,5,6],[7,8,9]]))
#print(s.findDiagonalOrder([[1,2,3],[4],[5,6,7],[8],[9,10,11]]))
#print(s.findDiagonalOrder([[1,2,3,4,5],[6,7],[8],[9,10,11],[12,13,14,15,16]]))
print(s.findDiagonalOrder([[11,6,9,20],[16,1,20],[14,19,14,17,15],[8,19,11,3],[3,13,17,4]]))

