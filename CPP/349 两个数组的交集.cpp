#include "include.hpp"
using namespace std;
/*
题目描述
349. 两个数组的交集
给定两个数组，编写一个函数来计算它们的交集。

 

示例 1：

输入：nums1 = [1,2,2,1], nums2 = [2,2]
输出：[2]
示例 2：

输入：nums1 = [4,9,5], nums2 = [9,4,9,8,4]
输出：[9,4]
 

说明：

输出结果中的每个元素一定是唯一的。
我们可以不考虑输出结果的顺序。
*/

class Solution {
public:
    vector<int> intersection(vector<int>& nums1, vector<int>& nums2) {
        unordered_map<int,int> dp;
        unordered_map<int,int> res;
        for(auto x:nums1)
        {
            dp[x]++;
        }
        for(auto x:nums2)
        {
            if(dp[x])
            {
                dp[x]--;
                res[x] = 1;
            }
        }
        vector<int> rtn;
        for(auto x:res)
        {
            rtn.push_back(x.first);
        }
        return rtn;
    }
};
int main()
{
    Solution s;
    system("pause");
};