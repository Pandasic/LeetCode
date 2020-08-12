#include "include.hpp"
using namespace std;
/*
题目描述
96. 不同的二叉搜索树
给定一个整数 n，求以 1 ... n 为节点组成的二叉搜索树有多少种？

示例:

输入: 3
输出: 5
解释:
给定 n = 3, 一共有 5 种不同结构的二叉搜索树:

   1         3     3      2      1
    \       /     /      / \      \
     3     2     1      1   3      2
    /     /       \                 \
   2     1         2                 3
通过次数58,200提交次数86,630
*/

/*动态规划*/
class Solution {
public:
    unordered_map<int,int> dp{(0,1),(1,1)};
    int numTrees(int n) {
        if(n <= 1) return 1;
        if(dp[n] != 0) return dp[n];
        int res = 0;
        n -=1;
        for(int i = 0;i <= n;i++)
        {
            res += numTrees(i)*numTrees(n-i);
        }
        dp[n + 1] = res;
        return res;
    }
};

/*数学公式*/
class Solution {
public:
    int numTrees(int n) {
        long long C = 1;
        for (int i = 0; i < n; ++i) {
            C = C * 2 * (2 * i + 1) / (i + 2);
        }
        return (int)C;
    }
};

int main()
{
    Solution s;
    system("pause");
};