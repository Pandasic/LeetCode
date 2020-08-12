#include "include.hpp"
using namespace std;
/*
200. 岛屿数量
给你一个由 '1'（陆地）和 '0'（水）组成的的二维网格，请你计算网格中岛屿的数量。

岛屿总是被水包围，并且每座岛屿只能由水平方向或竖直方向上相邻的陆地连接形成。

此外，你可以假设该网格的四条边均被水包围。

 

示例 1:

输入:
11110
11010
11000
00000
输出: 1
示例 2:

输入:
11000
11000
00100
00011
输出: 3
解释: 每座岛屿只能由水平和/或竖直方向上相邻的陆地连接而成。
通过次数121,031提交次数243,885

*/
class Solution {
public:
    int isLandIndex = 2;
    int w = 0,h = 0;
    int addx[4] = {1,0,-1,0};
    int addy[4] = {0,1,0,-1};

    int numIslands(vector<vector<char>>& grid) {
        h = grid.size();
        if (h != 0)
            w = grid[0].size();
        else
            return 0;
        for(int i = 0;i<h;++i)
        {
            for(int j= 0;j<w;++j)
            {
                if(grid[i][j] == '1')
                {
                    dfs(grid,j,i,isLandIndex);
                    ++isLandIndex;
                }
            }
        }
        return isLandIndex-2;
    }

    void dfs(vector<vector<char>>& grid,int x,int y,int index)
    {
        if(x<0 || x>=w || y<0 ||y >=h || grid[y][x] != '1')
            return;
        grid[y][x] = '0';
        for(int i=0;i<4;i++)
        {
            dfs(grid,x+addx[i],y+addy[i],index);
        }
    }
};