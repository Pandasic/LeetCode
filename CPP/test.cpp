#include "include.hpp"
using namespace std;
/*
试题 08.11. 硬币
硬币。给定数量不限的硬币，币值为25分、10分、5分和1分，编写代码计算n分有几种表示法。(结果可能会很大，你需要将结果模上1000000007)

示例1:

 输入: n = 5
 输出：2
 解释: 有两种方式可以凑成总金额:
5=5
5=1+1+1+1+1
示例2:

 输入: n = 10
 输出：4
 解释: 有四种方式可以凑成总金额:
10=10
10=5+5
10=5+1+1+1+1+1
10=1+1+1+1+1+1+1+1+1+1
说明：

注意:

你可以假设：

0 <= n (总金额) <= 1000000
*/


int main()
{

    int n = 0,m = 0;
    cin>>n>>m;
    vector<vector<int>> im(n,vector<int>(m,0));
    for(int i = 0;i <n;i++)
    {
        for(int j = 0;j <m;j++)
        {
            int v;
            cin >> im[i][j];
            cout<<im[i][j]<<endl;
        }
    }

};