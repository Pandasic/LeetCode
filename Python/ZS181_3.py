"""
5366. 检查网格中是否存在有效路径 显示英文描述 
用户通过次数157
用户尝试次数256
通过次数157
提交次数392
题目难度Medium
给你一个 m x n 的网格 grid。网格里的每个单元都代表一条街道。grid[i][j] 的街道可以是：

1 表示连接左单元格和右单元格的街道。
2 表示连接上单元格和下单元格的街道。
3 表示连接左单元格和下单元格的街道。
4 表示连接右单元格和下单元格的街道。
5 表示连接左单元格和上单元格的街道。
6 表示连接右单元格和上单元格的街道。


你最开始从左上角的单元格 (0,0) 开始出发，网格中的「有效路径」是指从左上方的单元格 (0,0) 开始、一直到右下方的 (m-1,n-1) 结束的路径。该路径必须只沿着街道走。

注意：你 不能 变更街道。

如果网格中存在有效的路径，则返回 true，否则返回 false 。

 

示例 1：



输入：grid = [[2,4,3],[6,5,2]]
输出：true
解释：如图所示，你可以从 (0, 0) 开始，访问网格中的所有单元格并到达 (m - 1, n - 1) 。
示例 2：



输入：grid = [[1,2,1],[1,2,1]]
输出：false
解释：如图所示，单元格 (0, 0) 上的街道没有与任何其他单元格上的街道相连，你只会停在 (0, 0) 处。
示例 3：

输入：grid = [[1,1,2]]
输出：false
解释：你会停在 (0, 1)，而且无法到达 (0, 2) 。
示例 4：

输入：grid = [[1,1,1,1,1,1,3]]
输出：true
示例 5：

输入：grid = [[2],[2],[2],[2],[2],[2],[6]]
输出：true
 

提示：

m == grid.length
n == grid[i].length
1 <= m, n <= 300
1 <= grid[i][j] <= 6
"""
X = 0
Y = 1
#坐标 （X,Y）
UP = (0,-1)
DOWN = (0,1)
LEFT = (-1,0)
RIGHT = (1,0)
M = 0
N = 0
class Solution:
    #道路枚举
    self.gridKind = \
    {
        1:(LEFT,RIGHT),
        2:(UP,DOWN),
        3:(LEFT,DOWN),
        4:(RIGHT,DONW),
        5:(LEFT,UP),
        6:(UP,RIGHT)
    }

    def hasValidPath(self, grid: List[List[int]]) -> bool:
        global M,N
        M = len(grid)
        N = len(grid[0])
        #记录地图 记录是否走过
        dp = [[False for j in range(m)] for i in range(n)]
        #当前 位置
        pos = [0,0]

        while pos != [m-1,n-1]:
            #可以行走的标志位
            pass

    def tryMove(self,pos,dp,addpos):
        canGoToNext = False
        #当前格标志位走过
        dp[pos[1],pos[0]] = True
        #走一端
        tpos = [pos[X] + addpos[X], pos[X],addpos[Y]]
        #tpos = [pos[X] + grid[pos[Y]][pos[X]][0][X],pos[X] + grid[pos[Y]][pos[X]][0][Y]]
        if tpos[X] >= M or tpos[X] <0:
            return None
        
        if tpos[Y] >= N or tpos[Y] <0:
            return None

        if dp[tpos[Y]][tpos[X]]
            