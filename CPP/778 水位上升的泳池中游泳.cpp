#include "include.hpp"
using namespace std;
/*
题目描述

778. 水位上升的泳池中游泳
在一个 N x N 的坐标方格 grid 中，每一个方格的值 grid[i][j] 表示在位置 (i,j) 的平台高度。

现在开始下雨了。当时间为 t 时，此时雨水导致水池中任意位置的水位为 t 。你可以从一个平台游向四周相邻的任意一个平台，但是前提是此时水位必须同时淹没这两个平台。假定你可以瞬间移动无限距离，也就是默认在方格内部游动是不耗时的。当然，在你游泳的时候你必须待在坐标方格里面。

你从坐标方格的左上平台 (0，0) 出发。最少耗时多久你才能到达坐标方格的右下平台 (N-1, N-1)？

 

示例 1:

输入: [[0,2],[1,3]]
输出: 3
解释:
时间为0时，你位于坐标方格的位置为 (0, 0)。
此时你不能游向任意方向，因为四个相邻方向平台的高度都大于当前时间为 0 时的水位。

等时间到达 3 时，你才可以游向平台 (1, 1). 因为此时的水位是 3，坐标方格中的平台没有比水位 3 更高的，所以你可以游向坐标方格中的任意位置
示例2:

输入: [[0,1,2,3,4],[24,23,22,21,5],[12,13,14,15,16],[11,17,18,19,20],[10,9,8,7,6]]
输出: 16
解释:
 0  1  2  3  4
24 23 22 21  5
12 13 14 15 16
11 17 18 19 20
10  9  8  7  6

最终的路线用加粗进行了标记。
我们必须等到时间为 16，此时才能保证平台 (0, 0) 和 (4, 4) 是连通的
 

提示:

2 <= N <= 50.
grid[i][j] 位于区间 [0, ..., N*N - 1] 内。
*/

/*
思路
本质上寻找可到达路径中的所有点的最大值的最小值*/
/*
基本方法是：计算每个水位t下，是否有起点[0,0]到终点[grid.size()-1, grid[0].size()-1]的可达路径。
在基本方法的基础上对水位t进行二分搜索来加速，left=grid[0][0], right=max(grid[i][j])，如果当前水位t = mid可达，则舍弃(mid，right]，若不可达则舍弃[left, mid];
通过简单的深度搜索就可以计算当前水位t是否是可达状态。
通过二分查找寻找可能边界
*/
class Solution {
public:
    int index[4][2] = {{1, 0}, {-1, 0}, {0, 1}, {0, -1}};
    int swimInWater(vector<vector<int>>& grid) {
        int left = grid[0][0], right = INT_MIN;
        for (int i = 0; i < grid.size(); ++i) {
            for (int j = 0; j < grid[0].size(); ++j) {
                right = max(right, grid[i][j]);
            }
        }
        while (left < right) {
            int mid = (left + right) / 2;
            vector<vector<int>> v(grid.size(), vector<int>(grid[0].size(), 0));
            if (dfs(grid, v, mid, 0, 0)) {
                right = mid;
            } else {
                left = mid + 1;
            }
        }
        return left;
    }

    bool dfs(vector<vector<int>>& grid, vector<vector<int>>& v, int h, int x, int y) {
        if (x == grid.size()-1 && y == grid[0].size()-1) return true;
        v[x][y] = 1;
        for (int i = 0; i < 4; ++i) {
            int xx = x + index[i][0];
            int yy = y + index[i][1];
            if (xx>=0&&xx<grid.size()&&yy>=0&&yy<grid[0].size()&&!v[xx][yy]&&grid[xx][yy]<=h) {
                if (dfs(grid, v, h, xx, yy)) return true;
            }
        }
        return false;
    }
};

int main()
{
    Solution s;
    system("pause");
};