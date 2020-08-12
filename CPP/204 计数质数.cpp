#include "include.hpp"
using namespace std;
/*
204. 计数质数
统计所有小于非负整数 n 的质数的数量。

示例:

输入: 10
输出: 4
解释: 小于 10 的质数一共有 4 个, 它们是 2, 3, 5, 7 。
*/


class Solution {
public:
    int countPrimes(int n) {
        if(n<2) return 0;
        vector<bool> dp(n,true);
        for(int i = 2;i <sqrt(n);i++)
        {
            if(!dp[i]) continue;
            for(int j = i*2;j<n;j+=i)
            {
                dp[j] = false;
            }
        }
        int rtn = -2;
        for(int v:dp)
        {
            rtn += v;
        }
        return rtn;
    }
};



int main()
{
    Solution s;
    s.countPrimes(2);
    
    system("pause");
};
