"""
56. 合并区间
给出一个区间的集合，请合并所有重叠的区间。

示例 1:

输入: [[1,3],[2,6],[8,10],[15,18]]
输出: [[1,6],[8,10],[15,18]]
解释: 区间 [1,3] 和 [2,6] 重叠, 将它们合并为 [1,6].
示例 2:

输入: [[1,4],[4,5]]
输出: [[1,5]]
解释: 区间 [1,4] 和 [4,5] 可被视为重叠区间。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/merge-intervals
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""

class Solution:
    def merge(self, intervals = []):
        if len(intervals) <= 1:
            return intervals
        intervals.sort(key = lambda x:x[0])
        index = 0
        while index < len(intervals) - 1:
            if intervals[index][1] >= intervals[index + 1][0]:
                if intervals[index][1] < intervals[index + 1][1]:
                    intervals.insert(index,[intervals[index][0],intervals[index + 1][1]])
                    del intervals[index + 2]
                    del intervals[index + 1]
                else:
                    del intervals[index + 1]
            else:
                index += 1
            print(index)
            print(intervals)
        return intervals

s = Solution()
print(s.merge([[1,4],[2,3]]))