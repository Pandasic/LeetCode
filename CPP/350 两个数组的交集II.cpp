#include "include.hpp"
using namespace std;
/*
350. 两个数组的交集 II
给定两个数组，编写一个函数来计算它们的交集。

示例 1:

输入: nums1 = [1,2,2,1], nums2 = [2,2]
输出: [2,2]
示例 2:

输入: nums1 = [4,9,5], nums2 = [9,4,9,8,4]
输出: [4,9]
说明：

输出结果中每个元素出现的次数，应与元素在两个数组中出现的次数一致。
我们可以不考虑输出结果的顺序。
进阶:

如果给定的数组已经排好序呢？你将如何优化你的算法？
如果 nums1 的大小比 nums2 小很多，哪种方法更优？
如果 nums2 的元素存储在磁盘上，磁盘内存是有限的，并且你不能一次加载所有的元素到内存中，你该怎么办？
通过次数102,072提交次数204,406
*/
/*哈希表*/
class Solution {
public:
    vector<int> intersect(vector<int>& nums1, vector<int>& nums2) {
        unordered_map<int,int> dp;
        vector<int> res;
        for(auto x:nums1)
        {
            dp[x]++;
        }
        for(auto x:nums2)
        {
            if(dp[x])
            {
                dp[x]--;
                res.push_back(x);
            }
        }
        return res;
    }
};

/*排序比较*/
class Solution {
public:
    vector<int> intersect(vector<int>& nums1, vector<int>& nums2) {
        sort(nums1.begin(),nums1.end());
        sort(nums2.begin(),nums2.end());
        int itor1=0, itor2=0;
        vector<int> res;
        while(itor1 < nums1.size() && itor2 < nums2.size())
        {
            if(nums1[itor1] == nums2[itor2])
            {
                res.push_back(nums1[itor1]);
                itor1++;
                itor2++;
            }
            else
            {
                if(nums1[itor1] < nums2[itor2])
                {
                    itor1++;
                }
                else
                {
                    itor2++;
                }
                
            }
            
        }
        return res;
    }
};



int main()
{
    Solution s;
    system("pause");
};