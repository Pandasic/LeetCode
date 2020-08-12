#include "include.hpp"
using namespace std;
/*
416. 分割等和子集
给定一个只包含正整数的非空数组。是否可以将这个数组分割成两个子集，使得两个子集的元素和相等。

注意:

每个数组中的元素不会超过 100
数组的大小不会超过 200
示例 1:

输入: [1, 5, 11, 5]

输出: true

解释: 数组可以分割成 [1, 5, 5] 和 [11].
 

示例 2:

输入: [1, 2, 3, 5]

输出: false

解释: 数组不能分割成两个元素和相等的子集.
 

通过次数39,975提交次数82,591
*/
/*回溯 超时*/
class Solution {
public:S
    bool canPartition(vector<int>& nums) {
        return _canPartition(nums,0,0);
    }
    bool _canPartition(vector<int>& nums,int itor,int sum) {
        if(itor == nums.size())
        {
            return sum == 0;
        }
        return _canPartition(nums,itor+1,sum+nums[itor]) 
        || _canPartition(nums,itor+1,sum-nums[itor]);
    }
};

/*动规*/
class Solution {
public:
    bool canPartition(vector<int>& nums){
        int sum = 0;
        for(int x :nums) sum+= x;
        if(sum%2 ) return false;
        return _canPartition(nums,sum>>1);
    }

    bool _canPartition(vector<int>& nums,int sum) {
        vector<vector<bool>> dp(nums.size(),vector<bool>(sum+1,false));
        for(int i = 0 ; i < nums.size() ; i++)
        {
            for(int s = 0 ; s <= sum ; s++)
            {   
                //s range [0, sum(nums)>>1]
                if(!i) 
                    dp[i][s] = (nums[i]==s);//i==0要单独求{ nums[0]一个元素和为s }
                else
                    dp[i][s] = dp[i-1][s] || (s-nums[i]>=0 ? dp[i-1][s-nums[i]] : false);
            }
        }
        return dp[nums.size()-1][sum];
    }
};


int main()
{
    Solution s;
    system("pause");
};