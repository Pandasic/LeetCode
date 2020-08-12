#include "include.hpp"
using namespace std;
/*
题目描述
315. 计算右侧小于当前元素的个数
给定一个整数数组 nums，按要求返回一个新数组 counts。数组 counts 有该性质： counts[i] 的值是  nums[i] 右侧小于 nums[i] 的元素的数量。

示例:

输入: [5,2,6,1]
输出: [2,1,1,0] 
解释:
5 的右侧有 2 个更小的元素 (2 和 1).
2 的右侧仅有 1 个更小的元素 (1).
6 的右侧有 1 个更小的元素 (1).
1 的右侧有 0 个更小的元素.
通过次数19,323提交次数50,331
在真实的面试中遇到过这道题？
*/
/*暴力法*/
class Solution {
public:
    vector<int> countSmaller(vector<int>& nums) {
        int len = nums.size();
        vector<int> res(len,0);
        for(int i = len - 1;i >= 0;i--)
        {
            for(int j = i+1 ; j< len;j++)
            {
                if(nums[j]< nums[i])
                {
                    res[i]++;
                }
            } 
        }
        return res;
    }
};
/*LeetCode 官方解 树状数组*/
class Solution {
private:
    vector<int> c;
    vector<int> a;

    //初始化容器
    void Init(int length) {
        c.resize(length, 0);
    }

    int LowBit(int x) {
        return x & (-x);
    }

    void Update(int pos) {
        while (pos < c.size()) {
            c[pos] += 1;
            pos += LowBit(pos);
        }
    }

    int Query(int pos) {
        int ret = 0;

        while (pos > 0) {
            ret += c[pos];
            pos -= LowBit(pos);
        }

        return ret;
    }

    void Discretization(vector<int>& nums) {
        a.assign(nums.begin(), nums.end());
        sort(a.begin(), a.end());
        a.erase(unique(a.begin(), a.end()), a.end());
    }
    
    int getId(int x) {
        return lower_bound(a.begin(), a.end(), x) - a.begin() + 1;
    }

public:
    vector<int> countSmaller(vector<int>& nums) {
        vector<int> resultList;

        Discretization(nums);

        Init(nums.size() + 5);
        
        for (int i = (int)nums.size() - 1; i >= 0; --i) {
            int id = getId(nums[i]);
            resultList.push_back(Query(id - 1));
            Update(id);
        }

        reverse(resultList.begin(), resultList.end());

        return resultList;
    }
};

/*索引数组 + 归并排序*/
class Solution {
public:
    vector<int> res;

    vector<int> countSmaller(vector<int>& vec) {

        if (vec.empty()){
            return {};
        }

        vector<pair<int, int>> nums;
        for (int i = 0; i < vec.size(); i++){
            nums.emplace_back(vec[i], i);
        }

        res = vector<int>(vec.size(), 0);
        merge_sort(nums, 0, (int)nums.size() - 1);

        return res;
    }

    void merge_sort(vector<pair<int, int>>& nums, int left, int right){
        if (left < right){
            int mid = left + (right - left) / 2;

            merge_sort(nums, left, mid);
            merge_sort(nums, mid + 1, right);
            merge(nums, left, mid, right);
        }
    }

    void merge(vector<pair<int, int>>& nums, int left, int mid, int right){
        int i = left, j = mid + 1;
        int k = left;

        vector<pair<int, int>> sort_nums;

        while (i <= mid && j <= right){
            if (nums[i].first <= nums[j].first){
                res[nums[i].second] += j - mid - 1;
                sort_nums.push_back(nums[i++]);
            }else if (nums[i].first > nums[j].first){
                sort_nums.push_back(nums[j++]);
            }
        }

        while (i <= mid){
            res[nums[i].second] += j - mid - 1;
            sort_nums.push_back(nums[i++]);
        }

        while (j <= right){
            sort_nums.push_back(nums[j++]);
        }

        for (int m = 0, n = left; m < sort_nums.size(); m++, n++){
            nums[n] = sort_nums[m];
        }
    }
};

int main()
{
    Solution s;
    system("pause");
};