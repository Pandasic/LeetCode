#include "include.hpp"
using namespace std;
/*
题目描述

54. 螺旋矩阵
给定一个包含 m x n 个元素的矩阵（m 行, n 列），请按照顺时针螺旋顺序，返回矩阵中的所有元素。

示例 1:

输入:
[
 [ 1, 2, 3 ],
 [ 4, 5, 6 ],
 [ 7, 8, 9 ]
]
输出: [1,2,3,6,9,8,7,4,5]
示例 2:

输入:
[
  [1, 2, 3, 4],
  [5, 6, 7, 8],
  [9,10,11,12]
]
输出: [1,2,3,4,8,12,11,10,9,5,6,7]
通过次数61,296提交次数152,348

*/
class Solution {
public:
    vector<int> spiralOrder(vector<vector<int>>& matrix) {
        if (matrix.size() == 0 || matrix[0].size() == 0)
            return vector<int>();
        int W = matrix[0].size(),H = matrix.size();

        vector<int> res;
        //当前圈的旋转位置
        int bw = 0,ew = W-1;
        int bh = 0,eh = H-1;

        while (true)
        {
            //横方向
            for(int i = bw;i<= ew ;i++)
            {
                res.push_back(matrix[bh][i]);
            }
            if(++bh >eh) break;
            for(int i = bh;i<= eh ;i++)
            {
                res.push_back(matrix[i][ew]);
            }
            if(--ew < bw) break;
            for(int i = ew;i>= bw ;i--)
            {
                res.push_back(matrix[eh][i]);
            }
            if(--eh < bh) break;
            for(int i = eh;i>= bh ;i--)
            {
                res.push_back(matrix[i][bw]);
            }
            if(++bw > ew) break;
        }
        return res;
    }
};
int main()
{
    Solution s;
    auto res = s.spiralOrder(
        vector<vector<int>>{
            vector<int>{1,2,3},
            vector<int>{4,5,6},
            vector<int>{7,8,9},
        }
    );
    for(auto x:res)
    {
        cout<<x<<" ";
    }
    system("pause");
};
