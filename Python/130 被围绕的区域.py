"""
130. 被围绕的区域
给定一个二维的矩阵，包含 'X' 和 'O'（字母 O）。

找到所有被 'X' 围绕的区域，并将这些区域里所有的 'O' 用 'X' 填充。

示例:

X X X X
X O O X
X X O X
X O X X
运行你的函数后，矩阵变为：

X X X X
X X X X
X X X X
X O X X
解释:

被围绕的区间不会存在于边界上，换句话说，任何边界上的 'O' 都不会被填充为 'X'。 任何不在边界上，或不与边界上的 'O' 相连的 'O' 最终都会被填充为 'X'。如果两个元素在水平或垂直方向相邻，则称它们是“相连”的。

通过次数30,493提交次数76,417
在真实的面试中遇到过这道题？
"""
import tools
class Solution:
    def solve(self, board) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        if len(board) == 0 or len(board[0]) == 0:
            return
        #DFS  深度优先搜索 Pos:X,Y
        def getConnect(board,pos):
            #try 边界检测
            try:
                if board[pos[1]][pos[0]] == "O":
                    board[pos[1]][pos[0]] = "#"
                    getConnect(board,(pos[0]+1,pos[1]))
                    getConnect(board,(pos[0]-1,pos[1]))
                    getConnect(board,(pos[0],pos[1]+1))
                    getConnect(board,(pos[0],pos[1]-1))
            except:
                return
        #思路 寻找边界上的O 不与边界上的O 相连的则为X
        for i in range(len(board[0])):
            getConnect(board,(i,0))
        for i in range(len(board[0])):
            getConnect(board,(i,len(board) - 1))
        for i in range(len(board)):
            getConnect(board,(len(board[0]) - 1,i))
        for i in range(len(board)):
            getConnect(board,(0,i))
        #print(tools.array2ToString(board))
        for r in range(len(board)):
            for c in range(len(board[0])):
                if board[r][c] == "O":
                    board[r][c] = "X"
                if board[r][c] == "#":
                    board[r][c] = "O"
        #print(tools.array2ToString(board))

s = Solution()
s.solve([["X","X","X","X"],["X","O","O","X"],["X","X","O","X"],["X","O","X","X"]])

