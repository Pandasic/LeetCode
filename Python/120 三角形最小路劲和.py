"""
120. 三角形最小路径和
给定一个三角形，找出自顶向下的最小路径和。每一步只能移动到下一行中相邻的结点上。

例如，给定三角形：

[
     [2],
    [3,4],
   [6,5,7],
  [4,1,8,3]
]
自顶向下的最小路径和为 11（即，2 + 3 + 5 + 1 = 11）。

说明：

如果你可以只使用 O(n) 的额外空间（n 为三角形的总行数）来解决这个问题，那么你的算法会很加分。

通过次数51,113提交次数79,487
"""

#动规
class Solution:
    def minimumTotal(self, triangle):
        dp = [[0 for i in range(len(triangle))] for i in range(len(triangle) + 1)]
        for r in range(1,len(triangle)+1):
            dp[r][0] = dp[r-1][0] + triangle[r-1][0]
            dp[r][r-1] = dp[r-1][r-2] + triangle[r-1][r-1]
            for j in range(1,r-1):
                dp[r][j] = min(
                    dp[r-1][j] + triangle[r - 1][j],
                    dp[r-1][j-1] + triangle[r - 1][j]
                )
        return min(dp[-1])

s = Solution()
s.minimumTotal(
    [
     [2],
    [3,4],
   [6,5,7],
  [4,1,8,3]
]
)