"""
给定一组不含重复元素的整数数组 nums，返回该数组所有可能的子集（幂集）。

说明：解集不能包含重复的子集。

示例:

输入: nums = [1,2,3]
输出:
[
  [3],
  [1],
  [2],
  [1,2,3],
  [1,3],
  [2,3],
  [1,2],
  []
]

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/subsets
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
#利用之前组合得思想 子集就是长度不等得组合
class mySolution:
    def subsets(self,nums):
        res = []
        N = len(nums)
        for i in range(N+1):
            arrIndexs = self.combine(N,i)
            for arrIndex in arrIndexs:
                part = []
                for v in arrIndex:
                    part.append(nums[v-1])
                res.append(part)
        return res

    def combine(self, n, k):
        def backtrack(first = 1, curr = []):
            # if the combination is done
            if len(curr) == k:  
                output.append(curr[:])
            for i in range(first, n + 1):
                # add i into the current combination
                curr.append(i)
                # use next integers to complete the combination
                backtrack(i + 1, curr)
                # backtrack
                curr.pop()
        
        output = []
        backtrack()
        return output

#再原有子集上覆盖
class Solution:
    def subsets(self,nums):
        res = [[],]

        for i in nums:
            new = []
            for v in res:
                t = v[:]
                t.append(i)
                new.append(t)
            res.extend(new)
        return res

s = Solution()
print(s.subsets([1,2,3]))