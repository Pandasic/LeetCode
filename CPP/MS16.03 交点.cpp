#include "include.hpp"
using namespace std;
/*
面试题 16.03. 交点
给定两条线段（表示为起点start = {X1, Y1}和终点end = {X2, Y2}），如果它们有交点，请计算其交点，没有交点则返回空值。

要求浮点型误差不超过10^-6。若有多个交点（线段重叠）则返回 X 值最小的点，X 坐标相同则返回 Y 值最小的点。

 

示例 1：

输入：
line1 = {0, 0}, {1, 0}
line2 = {1, 1}, {0, -1}
输出： {0.5, 0}
示例 2：

输入：
line1 = {0, 0}, {3, 3}
line2 = {1, 1}, {2, 2}
输出： {1, 1}
示例 3：

输入：
line1 = {0, 0}, {1, 1}
line2 = {1, 0}, {2, 1}
输出： {}，两条线段没有交点
 

提示：

坐标绝对值不会超过 2^7
输入的坐标均是有效的二维坐标
通过次数8,191提交次数18,022
*/
/*https://leetcode-cn.com/problems/intersection-lcci/solution/jiao-dian-by-leetcode-solution/*/


class Solution {
public:
    vector<double> intersection(vector<int>& start1, vector<int>& end1, vector<int>& start2, vector<int>& end2) {
        double DOUBLE_OFFSET = 10e-6;
        //斜率
        double d1 = (start1[0] - start1[2])/(start1[1] - start1[3]);
        double d2 = (start2[0] - start2[2])/(start2[1] - start2[3]);
        //两直线平行
        if(abs(d1-d2) <= DOUBLE_OFFSET)
        {
            // 线段是否重合
            if (abs(d1*(0-start1[0]) - start1[1] - d2*(0 - start2[0]) + start2[1]) <= DOUBLE_OFFSET)
            {    
                int minx =min(min(start1[0],start1[2]),min(start2[0],start2[2]));
                return vector<double>(minx,d1*(minx - start1[0])-start1[1]);
            }
            else
                return vector<double>();
        }
        else
        {
            //求交点
            double x = (d1*start1[0]+start1[1] - d2 * start2[0]-start2[1])/(d1 - d2);
            //交点是否在线段上
            if( x > min(start1[0],start1[2]) - DOUBLE_OFFSET
            &&  x < min(start1[0],start1[2]) + DOUBLE_OFFSET
            &&  x > min(start2[0],start2[2]) - DOUBLE_OFFSET
            &&  x < min(start2[0],start2[2]) + DOUBLE_OFFSET
            )
            {
                return vector<double>(x,d1*(x-start1[0]));
            }
        }
        
    }
};

int main()
{
    Solution s;
    cout<<10e-6;
    system("pause");
};