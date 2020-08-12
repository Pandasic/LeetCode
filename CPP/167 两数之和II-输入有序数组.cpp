 #include "include.hpp"
 using namespace std;
 /*
167. 两数之和 II - 输入有序数组
给定一个已按照升序排列 的有序数组，找到两个数使得它们相加之和等于目标数。

函数应该返回这两个下标值 index1 和 index2，其中 index1 必须小于 index2。

说明:

返回的下标值（index1 和 index2）不是从零开始的。
你可以假设每个输入只对应唯一的答案，而且你不可以重复使用相同的元素。
示例:

输入: numbers = [2, 7, 11, 15], target = 9
输出: [1,2]
解释: 2 与 7 之和等于目标数 9 。因此 index1 = 1, index2 = 2 。
通过次数113,983提交次数206,130
在真实的面试中遇到过这道题？
 */
/*迭代 + 二分查找*/
class Solution {
public:
    int binarySearch(vector<int>& numbers,int begin, int target)
    {
        int left = begin,right = numbers.size() - 1;
        while(left <= right)
        {
            int mid = left + (right - left)/2;
            if(numbers[mid] == target) return mid;
            else if (numbers[mid] > target) right = mid - 1;
            else if (numbers[mid] < target) left = mid + 1;
        }
        return -1;
    }

    vector<int> twoSum(vector<int>& numbers,int target) {
        if(numbers.size() <= 1) return vector<int>();
        for(int i = 0;i < numbers.size() ;i++)
        {
            int tar = binarySearch(numbers,i+1,target - numbers[i]);
            if(tar == -1) 
                continue;
            else
                return vector<int>{i+1,tar+1};
        }
        return  vector<int>();
    }
};

/*双指针*/
class Solution {
public:
    vector<int> twoSum(vector<int>& numbers, int target) {
        int left = 0,right = numbers.size() - 1;
        //保证集合个数为2 
        while(left < right)
        {
            int sum = numbers[left] + numbers[right];
            if(sum == target) return vector<int>{left+1,right+1};
            else if( sum > target) right--;
            else if(sum < target) left++;
        }
        return vector<int>{0,0};
    }
};

 int main()
 {
     Solution s;
     system("pause");
 };