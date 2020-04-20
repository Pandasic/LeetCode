"""
79. 单词搜索
给定一个二维网格和一个单词，找出该单词是否存在于网格中。

单词必须按照字母顺序，通过相邻的单元格内的字母构成，其中“相邻”单元格是那些水平相邻或垂直相邻的单元格。同一个单元格内的字母不允许被重复使用。

 

示例:

board =
[
  ['A','B','C','E'],
  ['S','F','C','S'],
  ['A','D','E','E']
]

给定 word = "ABCCED", 返回 true
给定 word = "SEE", 返回 true
给定 word = "ABCB", 返回 false
 

提示：

board 和 word 中只包含大写和小写英文字母。
1 <= board.length <= 200
1 <= board[i].length <= 200
1 <= word.length <= 10^3
通过次数46,547提交次数113,452
"""


#回溯 搜索
posAdd = [(-1,0),(1,0),(0,1),(0,-1)]
class Solution:
    def exist(self, board, word) -> bool:
        res = False
        for row in range(len(board)):
            for c in range(len(board[row])):
                #寻找起始点
                if board[row][c] == word[0]:
                    res |= self.walkInBoard(board,word,0,[(c,row)])
        return res

    def walkInBoard(self,board,word,itor,path):
        """
        board : 棋盘
        word : 要寻找得单词
        itor : 当前找到得下表
        path : 已经走过得路径
        """

        #当前坐标
        nowPos = path[-1]
        if word[itor] != board[nowPos[1]][nowPos[0]]:
            return False

        if len(path) == len(word):
            return True

        res = False
        #移动寻找得坐标
        for vec in posAdd:
            newPos = (nowPos[0] - vec[0],nowPos[1] + vec[1])
            if 0<= newPos[1] <len(board) and \
            0<= newPos[0]< len(board[0]):
                if newPos not in path:
                    res |= self.walkInBoard(board,word,itor + 1,path[:] + [newPos])
        return res

#CPP
"""
bool dfs (vector<vector<char>>& board, string& word,
         int size, int x, int y, vector<vector<int>>& f){
    if (size == word.size()){
        return true;
    }//outofbound
    if (x < 0 || x >= board.size() 
       || y < 0 || y > board[0].size() 
       || board[x][y] != word[size]){
        return false;
    }
    if (f[x][y] == 0) {
        f[x][y] = 1;
        if (dfs(board, word, size+1, x+1, y, f) 
           || dfs(board, word, size+1, x-1, y, f) 
           || dfs(board, word, size+1, x, y+1, f) 
           || dfs(board, word, size+1, x, y-1, f)){
            return true;
        }
        f[x][y] = 0;
    }
    return false;
}

bool exist(vector<vector<char>>& board, string word) {
    if (board.empty() || word.empty()){
        return false;
    }
    int row = board.size(), col = board[0].size();
    vector<vector<int>> f(row, vector<int>(col, 0));
    for (int i = 0; i < row; ++i){
        for (int j = 0; j < col; ++j){
            if (dfs(board, word, 0, i,j, f)){
                return true;
            }
        }
    }
    return false;
}

"""

s = Solution()
board =\
[
  ['A','B','C','E'],
  ['S','F','C','S'],
  ['A','D','E','E']
]

#print(s.exist(board,"ABCCED"))
#print(s.exist(board,"SEE"))
print(s.exist(board,"ABCB"))
