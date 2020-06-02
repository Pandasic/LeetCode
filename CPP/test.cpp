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

/*
 思路
 比较函数学到了 
 就是先转换成字符串
 然后比较排序
 最后拼接；
 记得最后去0
*/
class Solution {
    static bool cmp(const string &a,const string &b){
        return a+b>b+a;
    }
public:
    string largestNumber(vector<int>& nums) {
        if(!nums.size()) return "";
        vector<string>vec;
        for(int num : nums){
            vec.push_back(to_string(num));
        }
        sort(vec.begin(),vec.end(),cmp);
        stringstream ss;
        string res;
        for(string str : vec){
            ss<<str;
        }
        ss>>res;
        return res[0]=='0'?"0":res;
    }
};

int main()
{
    Solution s;
    vector<int> n{};
    cout<<s.largestNumber(n);
    system("pause");
};