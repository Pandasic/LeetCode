"""
5399. 数位成本和为目标值的最大数字 显示英文描述 
通过的用户数32
尝试过的用户数45
用户总通过次数38
用户总提交次数70
题目难度Hard
给你一个整数数组 cost 和一个整数 target 。请你返回满足如下规则可以得到的 最大 整数：

给当前结果添加一个数位（i + 1）的成本为 cost[i] （cost 数组下标从 0 开始）。
总成本必须恰好等于 target 。
添加的数位中没有数字 0 。
由于答案可能会很大，请你以字符串形式返回。

如果按照上述要求无法得到任何整数，请你返回 "0" 。

 

示例 1：

输入：cost = [4,3,2,5,6,7,2,5,5], target = 9
输出："7772"
解释：添加数位 '7' 的成本为 2 ，添加数位 '2' 的成本为 3 。所以 "7772" 的代价为 2*3+ 3*1 = 9 。 "997" 也是满足要求的数字，但 "7772" 是较大的数字。
 数字     成本
  1  ->   4
  2  ->   3
  3  ->   2
  4  ->   5
  5  ->   6
  6  ->   7
  7  ->   2
  8  ->   5
  9  ->   5
示例 2：

输入：cost = [7,6,5,5,5,6,8,7,8], target = 12
输出："85"
解释：添加数位 '8' 的成本是 7 ，添加数位 '5' 的成本是 5 。"85" 的成本为 7 + 5 = 12 。
示例 3：

输入：cost = [2,4,6,2,4,6,4,4,4], target = 5
输出："0"
解释：总成本是 target 的条件下，无法生成任何整数。
示例 4：

输入：cost = [6,10,15,40,40,40,40,40,40], target = 47
输出："32211"
 

提示：

cost.length == 9
1 <= cost[i] <= 5000
1 <= target <= 5000
"""

class Solution:
    def __init__(self):
        self.maxVal = "0"
        self.maxDepth = 0
        self.dp = {}

    def largestNumber(self, cost, target) -> str:
        #尽可能多的选取
        #尽可能大的选取
        costPair = {}
        for i in range(len(cost)-1,-1,-1):
            if cost[i] not in costPair:
                costPair[cost[i]] = i+1
        costPair = [item for item in costPair.items()]
        costPair.sort()

        res = self.largestNumberPart(costPair,target,0)
        if res == None:
            return "0"
        else:
            return res
    
    def largestNumberPart(self, cost, target,depth) -> str:
        if target == 0:
            if depth >= self.maxDepth:
                self.maxDepth = depth
                return ""
            else:
                return None
        if target < 0 :
            return None
        maxStr = None
        for ncost,val in cost:
            p = self.largestNumberPart(cost,target - ncost,depth+1)
            if p != None:
                p += str(val)
                maxStr = self.strMax(maxStr,p)
        return maxStr


    def strMax(self,s1,s2):
        if s1 == None and s2 ==None:
            return None
        if s1 == None: 
            return s2
        if s2 == None:
            return s1
        
        if len(s1) > len(s2):
            return s1
        elif len(s1) < len(s2):
            return s2
        else:
            for i in range(len(s1)):
                if s1[i] > s2[i]:
                    return s1
                elif s1[i] < s2[i]:
                    return s2
            return s1
            
s = Solution()
print(s.largestNumber([4,3,2,5,6,7,2,5,5],9))
print(s.largestNumber([2,4,6,2,4,6,4,4,4],5))
print(s.largestNumber([6,10,15,40,40,40,40,40,40],47))
print(s.largestNumber([1,1,1,1,1,1,1,3,2],10))