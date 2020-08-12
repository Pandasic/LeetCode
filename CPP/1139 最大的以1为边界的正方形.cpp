#include "include.hpp"
using namespace std;
/*
1139. 最大的以 1 为边界的正方形
给你一个由若干 0 和 1 组成的二维网格 grid，请你找出边界全部由 1 组成的最大 正方形 子网格，并返回该子网格中的元素数量。如果不存在，则返回 0。

 

示例 1：

输入：grid = [[1,1,1],[1,0,1],[1,1,1]]
输出：9
示例 2：

输入：grid = [[1,1,0,0]]
输出：1
 

提示：

1 <= grid.length <= 100
1 <= grid[0].length <= 100
grid[i][j] 为 0 或 1
通过次数5,047提交次数11,107
*/

class Solution {
public:
    int largest1BorderedSquare(vector<vector<int>>& grid) {
        int w = grid[0].size(),h = grid.size();
        vector<vector<vector<int>>> dp(h+1,vector<vector<int>>(w+1,{0,0}));
        int res = 0;
        for(int i = 1;i < h+1;i++)
        {
            cout<<endl;
            for(int j = 1;j < w+1;j++)
            {
                if(grid[i - 1][j - 1])
                {
                    dp[i][j][0] = dp[i][j-1][0] + 1;
                    dp[i][j][1] = dp[i-1][j][1] + 1;
                    int t = min(dp[i][j][0],dp[i][j][1]);
                    cout<<t<<' ';
                    for(int z = t;z >= max(res,0); z--)
                    {
                        if(dp[i][j-z][1] >= z+1 &&  dp[i-z][j][0] >= z+1)
                        {
                            res = max(res,z+1);
                            break;
                        }
                    }
                }
                else
                    cout<<0<<' ';
            }
        }
        return res*res;
    }
};

int main()
{
    Solution s;
    system("pause");
};