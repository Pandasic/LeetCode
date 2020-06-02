#include "include.hpp"
using namespace std;
/*
题目描述
179. 最大数
给定一组非负整数，重新排列它们的顺序使之组成一个最大的整数。

示例 1:

输入: [10,2]
输出: 210
示例 2:

输入: [3,30,34,5,9]
输出: 9534330
说明: 输出结果可能非常大，所以你需要返回一个字符串而不是整数。

通过次数31,068提交次数85,807
在真实的面试中遇到过这道题？
*/

class Solution {
    public:
    /*function*/
    string largestNumber(vector<int>& nums) {
        vector<string> strNums;
        for(int v:nums)
        {
            strNums.push_back(to_string(v));
        }
        sort(strNums.begin(),strNums.end(),greater<>());
        string res("");
        for(string v:strNums)
        {
            res = res.append(v);
        }
        return res;
    }
};

int main()
{
    Solution s;
    s.largestNumber(vector<int>{3,30,34,5,9});
    system("pause");
};