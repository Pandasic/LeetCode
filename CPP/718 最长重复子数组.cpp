#include "include.hpp"
using namespace std;
/*
题目描述
718. 最长重复子数组
给两个整数数组 A 和 B ，返回两个数组中公共的、长度最长的子数组的长度。

示例 1:

输入:
A: [1,2,3,2,1]
B: [3,2,1,4,7]
输出: 3
解释: 
长度最长的公共子数组是 [3, 2, 1]。
说明:

1 <= len(A), len(B) <= 1000
0 <= A[i], B[i] < 100
*/

/*暴力*/
class Solution {
public:
    int findLength(vector<int>& A, vector<int>& B) {
        int maxLen = 0;
        for(int i = 0;i<A.size();i++)
        {
            for(int j = 0;j < B.size();j++)
            {
                if (A[i] == B[j])
                {
                    int k = 0;
                    for(k = 0; k < min(A.size()-i,B.size()-j);k++)
                    {
                        if(A[i+k] != B[j+k])
                            break;
                    }
                    maxLen = max(maxLen,k);
                }
            }
        }
        return maxLen;
    }
};


class Solution {
public:
    int findLength(vector<int>& A, vector<int>& B) {
        int maxLen = 0;
        for(int i = 0;i<A.size();i++)
        {
            for(int j = 0;j < B.size();j++)
            {
                if (A[i] == B[j])
                {
                    int k = 0;
                    for(k = 0; k < min(A.size()-i,B.size()-j);k++)
                    {
                        if(A[i+k] != B[j+k])
                            break;
                    }
                    maxLen = max(maxLen,k);
                }
            }
        }
        return maxLen;
    }
};

/*动规*/
class Solution2{
public:
    int findLength(vector<int>& A, vector<int>& B) {
        int lenA = A.size(),lenB = B.size();
        //vector<vector<int>> dp(lenA+1,vector<int>(lenB+1,0));
        int dp[1001][1001];
        int maxLen = 0;
        for(int i = 0; i < lenA;i++)
        {
            for(int j = 0;j < lenB;j++)
            {
                dp[i+1][j+1] = A[i] == B[j] ? dp[i][j] + 1:0;
                maxLen = max(dp[i+1][j+1],maxLen);
            }
        }
        return maxLen;
    }
};

/*滑动窗口*/
class Solution3{
public:
    int m = 0,n = 0;
    int maxLength(vector<int>& A, vector<int>& B, int addA, int addB, int len) {
        int ret = 0, k = 0;
        for (int i = 0; i < len; i++) {
            if (A[addA + i] == B[addB + i]) {
                k++;
            } else {
                k = 0;
            }
            ret = max(ret, k);
        }
        return ret;
    }

    int findLength(vector<int>& A, vector<int>& B)
    {
        m = A.size();
        n = B.size();
        int stepLen = m + n -1 ;
        int rtn =0;
        for (int i = 0; i < stepLen; i++) {
        //下面一大坨主要判断数组A和数组B比较的起始位置和比较的长度
            int aStart = 0;
            int bStart = 0;
            int len = 0;
            if (i < m) {
                aStart = m - i - 1;
                bStart = 0;
                len = i + 1;
            } else {
                aStart = 0;
                bStart = i - m;
                len = min(n - bStart, m);
            }
            int maxlen = maxLength(A, B, aStart, bStart, len);
            rtn = max(rtn, maxlen);
        }
        return rtn;
    }
};

int main()
{
    Solution s;
    system("pause");
};