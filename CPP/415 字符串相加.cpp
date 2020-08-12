#include "include.hpp"
using namespace std;
/*
415. 字符串相加
给定两个字符串形式的非负整数 num1 和num2 ，计算它们的和。

注意：

num1 和num2 的长度都小于 5100.
num1 和num2 都只包含数字 0-9.
num1 和num2 都不包含任何前导零。
你不能使用任何內建 BigInteger 库， 也不能直接将输入的字符串转换为整数形式。
通过次数49,870提交次数97,650
在真实的面试中遇到过这道题？
*/

/*迭代相加*/
class Solution {
public:
    string addStrings(string num1, string num2) {
        int itor1 = num1.size() - 1,itor2 = num2.size() - 1;
        string res = "";
        int add = 0,mod = 0;
        while(itor2 >= 0 || itor1 >= 0)
        {
            int v = (itor1>=0?num1[itor1--] - '0':0) + (itor2>=0?num2[itor2--] - '0':0) + add;
            add = v / 10;
            mod = v % 10;
            res.push_back(mod + '0');
        }
        if (add > 0)
            res.push_back(add + '0');
        reverse(res.begin(),res.end());
        return res;
    }
};
int main()
{
    Solution s;
    system("pause");
};