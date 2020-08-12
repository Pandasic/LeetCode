#include "include.hpp"
using namespace std;
/*
1470. 重新排列数组
给你一个数组 nums ，数组中有 2n 个元素，按 [x1,x2,...,xn,y1,y2,...,yn] 的格式排列。

请你将数组按 [x1,y1,x2,y2,...,xn,yn] 格式重新排列，返回重排后的数组。

 

示例 1：

输入：nums = [2,5,1,3,4,7], n = 3
输出：[2,3,5,4,1,7] 
解释：由于 x1=2, x2=5, x3=1, y1=3, y2=4, y3=7 ，所以答案为 [2,3,5,4,1,7]
示例 2：

输入：nums = [1,2,3,4,4,3,2,1], n = 4
输出：[1,4,2,3,3,2,4,1]
示例 3：

输入：nums = [1,1,2,2], n = 2
输出：[1,2,1,2]
 

提示：

1 <= n <= 500
nums.length == 2n
1 <= nums[i] <= 10^3
通过次数14,726提交次数16,966
在真实的面试中遇到过这道题？
*/

class Solution {
public:
    int deleteAndEarn(vector<int>& nums) {
        if(nums.size() < 1) return 0;
        int maxn = 0;
        for(int it : nums)
            maxn = max(maxn, it);
        vector<int> cnt(maxn+1), dp(maxn+1);
        for(int it : nums)
            cnt[it]++;
        dp[1] = cnt[1];
        for(int i = 2; i <= maxn; i++)
            dp[i] = max(dp[i-1], dp[i-2] + cnt[i] * i);
        return dp[maxn];
    }
};

int main()
{
    Solution s;
    system("pause");
};