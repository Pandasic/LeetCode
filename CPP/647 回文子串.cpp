#include "include.hpp"
using namespace std;
/*
647. 回文子串
给定一个字符串，你的任务是计算这个字符串中有多少个回文子串。

具有不同开始位置或结束位置的子串，即使是由相同的字符组成，也会被视作不同的子串。

 

示例 1：

输入："abc"
输出：3
解释：三个回文子串: "a", "b", "c"
示例 2：

输入："aaa"
输出：6
解释：6个回文子串: "a", "a", "a", "aa", "aa", "aaa"
 

提示：

输入的字符串长度不会超过 1000 。
通过次数43,363提交次数68,036
*/
//枚举所有结果
class Solution {
public:
    int countSubstrings(string s) {
        int len = s.size();
        int res = 0;
        for(int  i = 0; i < len;i++)
        {
            for(int j = 1 ; j < len - i + 1;j++)
            {
                string sub = s.substr(i,j);
                string cp = sub;
                reverse(sub.begin(),sub.end());
                cout<<sub<<" "<<cp<<endl;
                if(sub == cp) ++res;
            }
        }
        return res;
    }
};

//中心拓展
class Solution {
public:
    int countSubstrings(string s) {
        int n = s.size(), ans = 0;
        for (int i = 0; i < 2 * n - 1; ++i) {
            int l = i / 2, r = i / 2 + i % 2;
            while (l >= 0 && r < n && s[l] == s[r]) {
                --l;
                ++r;
                ++ans;
            }
        }
        return ans;
    }
};

int main()
{
    Solution s;
    cout<<s.countSubstrings("abc");
    system("pause");
};