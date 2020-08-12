#include "include.hpp"
using namespace std;
/*
题目描述
64. 最小路径和
给定一个包含非负整数的 m x n 网格，请找出一条从左上角到右下角的路径，使得路径上的数字总和为最小。

说明：每次只能向下或者向右移动一步。

示例:

输入:
[
  [1,3,1],
  [1,5,1],
  [4,2,1]
]
输出: 7
解释: 因为路径 1→3→1→1→1 的总和最小。
*/
class Solution {
public:
    int minPathSum(vector<vector<int>>& grid) {
        int  h =grid.size(),w;
        if(h > 0)
            w = grid[0].size();
        else
            return 0;
        if(w<= 0)
            return 0;
        
        for(int i = 1;i < h;i++)
            grid[i][0] += grid[i-1][0];
        for(int i = 1;i < w;i++)
            grid[0][i] += grid[0][i-1];

        for(int i = 1;i < h;i++)
        {
            for(int j = 1;j<w;j++)
            {
                grid[i][j] += min(grid[i-1][j],grid[i][j-1]);
            }
            cout<<endl;
        }
        return grid[h-1][w-1];
    }
};

int main()
{
    Solution s;
    system("pause");
};