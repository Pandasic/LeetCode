"""
一个机器人位于一个 m x n 网格的左上角 （起始点在下图中标记为“Start” ）。

机器人每次只能向下或者向右移动一步。机器人试图达到网格的右下角（在下图中标记为“Finish”）。

现在考虑网格中有障碍物。那么从左上角到右下角将会有多少条不同的路径？



网格中的障碍物和空位置分别用 1 和 0 来表示。

说明：m 和 n 的值均不超过 100。

示例 1:

输入:
[
  [0,0,0],
  [0,1,0],
  [0,0,0]
]
输出: 2
解释:
3x3 网格的正中间有一个障碍物。
从左上角到右下角一共有 2 条不同的路径：
1. 向右 -> 向右 -> 向下 -> 向下
2. 向下 -> 向下 -> 向右 -> 向右

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/unique-paths-ii
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
import numpy as np
#动规解题 数的值=左+上的值之和 遇到障碍则为0
class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid):
        if obstacleGrid[0][0] == 1:
            return 0
        w = len(obstacleGrid[0])
        h = len(obstacleGrid)
        # 数组初始化
        dp = [ [-1]* (w + 1)\
        for i in range((h + 1))]

        for i in range(w + 1):
            dp[0][i] = 0
        
        for i in range(h + 1):
            dp[i][0] = 0

        for y in range(h):
            for x in range(w):
                if x == 0 and y == 0:
                    dp[y+1][x+1] = 1
                    continue
                if obstacleGrid[y][x] == 1:
                    dp[y+1][x+1] = 0
                else:
                    dp[y+1][x+1] = dp[y][x+1] + dp[y+1][x]
                #print(np.array(dp))
        return dp[-1][-1]

s = Solution()
print( 
    s.uniquePathsWithObstacles(
        [
            [0,0,0],
            [0,1,0],
            [0,0,0]
        ])
)

print( 
    s.uniquePathsWithObstacles(
        [
            [0,0,0,0],
            [0,1,0,0],
            [0,0,0,0]
        ])
)
print( 
    s.uniquePathsWithObstacles(
        [
            [0,0,0,0],
            [0,1,0,0],
            [0,0,0,0]
        ])
)