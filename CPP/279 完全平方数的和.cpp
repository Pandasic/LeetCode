#include "include.hpp"
using namespace std;
/*
题目描述
*/

class Solution {
public:
    int numSquares(int n) {


        vector<int> dp(n+1,9999);
        dp[0] = 0;
        for(int i = 1;i<=n;i++)
        {
            for(int j = 1;j*j <= i;j++)
            {
                dp[i] = min(dp[i],dp[i-j*j]+1);
            }
        }
        return dp[n];
    }
};

int main()
{
    Solution s;
    system("pause");
};