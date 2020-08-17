#include "include.hpp"
using namespace std;
/*
43. 字符串相乘
给定两个以字符串形式表示的非负整数 num1 和 num2，返回 num1 和 num2 的乘积，它们的乘积也表示为字符串形式。

示例 1:

输入: num1 = "2", num2 = "3"
输出: "6"
示例 2:

输入: num1 = "123", num2 = "456"
输出: "56088"
说明：

num1 和 num2 的长度小于110。
num1 和 num2 只包含数字 0-9。
num1 和 num2 均不以零开头，除非是数字 0 本身。
不能使用任何标准库的大数类型（比如 BigInteger）或直接将输入转换为整数来处理。
通过次数91,094提交次数207,731
在真实的面试中遇到过这道题？
*/

class Solution {
public:
    string multiply(string num1, string num2) {
        vector<int> dp(300,0);
        int val1 = 0,val2 = 0;
        reverse(num1.begin(),num1.end());
        reverse(num2.begin(),num2.end());
        for(int i = 0; i < num1.size() ;i++)
        {
            val1 = num1[i] - '0';
            for(int j = 0; j < num2.size() ;j++)
            {
                val2 = num2[j] - '0';
                dp[ i+j ] += val1 * val2;

            }
        }
        string res = "";
        for(int i = 0;i <300 - 1;i++)
        {
            res += '0' + dp[i] % 10;
            dp[i+1] += dp[i]/10; 
        }

        reverse(res.begin(),res.end());

        for(int i = 0;i<res.size();i++)
        {
            if(res[i] != '0')
            {
                return res.substr(i,res.size());
            }
        }
        return "0";
    }

};
int main()
{
    Solution s;
    system("pause");
};