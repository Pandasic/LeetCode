#include "include.hpp"
using namespace std;
/*
题目描述
17. 电话号码的字母组合
给定一个仅包含数字 2-9 的字符串，返回所有它能表示的字母组合。

给出数字到字母的映射如下（与电话按键相同）。注意 1 不对应任何字母。



示例:

输入："23"
输出：["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"].
说明:
尽管上面的答案是按字典序排列的，但是你可以任意选择答案输出的顺序。

*/

class Solution {
public:
std::unordered_map<int,int>
    vector<string> letterCombinations(string digits) {
        if(digits.size() == 0) return vector<string>{};
        unordered_map<char,vector<char>> remap;
        remap['2'] = vector<char>{'a','b','c'};
        remap['3'] = vector<char>{'d','e','f'};
        remap['4'] = vector<char>{'g','h','i'};
        remap['5'] = vector<char>{'j','k','l'};
        remap['6'] = vector<char>{'m','n','o'};
        remap['7'] = vector<char>{'p','q','r','s'};
        remap['8'] = vector<char>{'t','u','v'};
        remap['9'] = vector<char>{'w','x','y','z'};
        vector<string> res{""};

        for(char num:digits)
        {
            vector<string> temp;
            for(string s:res)
            {
                for(char a:remap[num])
                {

                    temp.push_back(s + a);
                }
            }
            res = temp;
        }
        return res;
    }
};

int main()
{
    Solution s;
    system("pause");
};