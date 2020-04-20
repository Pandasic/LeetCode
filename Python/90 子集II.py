"""
90. 子集 II
给定一个可能包含重复元素的整数数组 nums，返回该数组所有可能的子集（幂集）。

说明：解集不能包含重复的子集。

示例:

输入: [1,2,2]
输出:
[
  [2],
  [1],
  [1,2,2],
  [2,2],
  [1,2],
  []
]
通过次数27,149提交次数45,664
"""
#想法 用set()  去重 再用78 做
class mySolution:
    def subsetsWithDup(self,nums):
        res = set()

        for i in nums:
            new = []
            for v in res:
                t = v[:]
                t.append(i)
                new.append(tuple(t))
            res.add(new)
        return res

# 刚开始我们只有空集一个答案，循环所有可能的数字，每次循环我们对当前答案的每一种情况考虑加入从1到上限次该数字并更新答案即可
class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        dic = {}
        for i in nums:
            dic[i] = dic.get(i, 0) + 1
        res = [[]]
        for i, v in dic.items():
            temp = res.copy()
            for j in res:
                temp.extend(j+[i]*(k+1) for k in range(v))
            res = temp
        return res

