"""
给出一个无重叠的 ，按照区间起始端点排序的区间列表。

在列表中插入一个新的区间，你需要确保列表中的区间仍然有序且不重叠（如果有必要的话，可以合并区间）。

示例 1:

输入: intervals = [[1,3],[6,9]], newInterval = [2,5]
输出: [[1,5],[6,9]]
示例 2:

输入: intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]], newInterval = [4,8]
输出: [[1,2],[3,10],[12,16]]
解释: 这是因为新的区间 [4,8] 与 [3,5],[6,7],[8,10] 重叠

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/insert-interval
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
'''
基于上次的合并= = 
'''
class Solution:
    def insert(self, intervals, newInterval):
        intervals.append(newInterval)
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
#别人家的代码 = =
class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        result = []
        i = 0
        while i < len(intervals) and intervals[i][1] < newInterval[0]:
            result.append(intervals[i])
            i += 1
        
        while i < len(intervals) and intervals[i][0] <= newInterval[1]:
            left = min(intervals[i][0], newInterval[0])
            right = max(intervals[i][1], newInterval[1])
            newInterval = [left, right]
            i += 1
        result.append(newInterval)
        
        while i < len(intervals):
            result.append(intervals[i])
            i += 1
        
        return result
            
               

s = Solution()
print(s.insert(
    [[1,2],[3,5],[6,7],[8,10],[12,16]],
    [4,8]))

