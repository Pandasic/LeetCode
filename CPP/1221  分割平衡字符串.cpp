#include "include.hpp"
using namespace std;
/*
题目描述
1221. 分割平衡字符串
在一个「平衡字符串」中，'L' 和 'R' 字符的数量是相同的。

给出一个平衡字符串 s，请你将它分割成尽可能多的平衡字符串。

返回可以通过分割得到的平衡字符串的最大数量。

 

示例 1：

输入：s = "RLRRLLRLRL"
输出：4
解释：s 可以分割为 "RL", "RRLL", "RL", "RL", 每个子字符串中都包含相同数量的 'L' 和 'R'。
示例 2：

输入：s = "RLLLLRRRLR"
输出：3
解释：s 可以分割为 "RL", "LLLRRR", "LR", 每个子字符串中都包含相同数量的 'L' 和 'R'。
示例 3：

输入：s = "LLLLRRRR"
输出：1
解释：s 只能保持原样 "LLLLRRRR".
 

提示：

1 <= s.length <= 1000
s[i] = 'L' 或 'R'
分割得到的每个字符串都必须是平衡字符串。
通过次数18,829提交次数24,026
*/
/*
简单的出入操作 有贪心
看了评论 感觉题目还是有点问题
*/
class Solution {
public:
    int balancedStringSplit(string s) {
        int flag = 0,res = 0;
        for(auto x:s)
        {
            if(x == 'L')
                --flag;
            if(x == 'R')
                ++flag;
            if(flag == 0)
                ++res;
        }
        return res; 
    }
};
int main()
{
    Solution s;
    system("pause");
};