#include "include.hpp"
using namespace std;
/*
1314. 矩阵区域和
给你一个 m * n 的矩阵 mat 和一个整数 K ，请你返回一个矩阵 answer ，其中每个 answer[i][j] 是所有满足下述条件的元素 mat[r][c] 的和： 

i - K <= r <= i + K, j - K <= c <= j + K 
(r, c) 在矩阵内。
 

示例 1：

输入：mat = [[1,2,3],[4,5,6],[7,8,9]], K = 1
输出：[[12,21,16],[27,45,33],[24,39,28]]
示例 2：

输入：mat = [[1,2,3],[4,5,6],[7,8,9]], K = 2
输出：[[45,45,45],[45,45,45],[45,45,45]]
 

提示：

m == mat.length
n == mat[i].length
1 <= m, n, K <= 100
1 <= mat[i][j] <= 100
*/

class Solution {
public:
    vector<vector<int>> matrixBlockSum(vector<vector<int>>& mat, int K) {
        int m = mat.size(),n = mat[0].size();
        vector<vector<int>> res(m,vector<int>(n,0));
        for(int i = 0; i < m;i++)
        {
            for(int j = 0; j < n;j++)
            {
                for(int r = i - K; r <= i + K ;r++)
                {
                    for(int c = j - K; c <= j+K; c++)
                    {
                        if(r < m && r >= 0 && c < n && c>= 0)
                        {
                            res[i][j] += mat[r][c];
                        }
                    }
                }
            }
        }
        return res;
    }
};

class Solution {
public:
    vector<vector<int>> matrixBlockSum(vector<vector<int>>& mat, int K) {
        int m = mat.size(),n = mat[0].size();
        vector<vector<int>> res(m + K,vector<int>(n + K,0));
        for(int i = 1; i < m;i++)
        {
            mat[i][0] += mat[i-1][0];
        }
        for(int j = 1; j < n;j++)
        {
            mat[0][j] += mat[0][j-1];
        }
        for(int i = 1; i < m;i++)
        {
            for(int j = 1; j < n;j++)
            {
                mat[i][j] +=  mat[i-1][j] + mat[i][j-1];;
            }
        }
        for(int i = K; i < m + K;i++)
        {
            for(int j = K; j < n + K;j++)
            {
                res[i][j] +=  mat[i+K][j+K] - mat[i + K][j - K] - mat[i - L][j + k] + mat[i - K][i - K];
            }
        }
        return res;
    }
};

class Solution {
public:
    int get(const vector<vector<int>>& pre, int m, int n, int x, int y) {
        x = max(min(x, m), 0);
        y = max(min(y, n), 0);
        return pre[x][y];
    }
    
    vector<vector<int>> matrixBlockSum(vector<vector<int>>& mat, int K) {
        int m = mat.size(), n = mat[0].size();
        vector<vector<int>> P(m + 1, vector<int>(n + 1));
        for (int i = 1; i <= m; ++i) {
            for (int j = 1; j <= n; ++j) {
                P[i][j] = P[i - 1][j] + P[i][j - 1] - P[i - 1][j - 1] + mat[i - 1][j - 1];
            }
        }
        
        vector<vector<int>> ans(m, vector<int>(n));
        for (int i = 0; i < m; ++i) {
            for (int j = 0; j < n; ++j) {
                ans[i][j] = get(P, m, n, i + K + 1, j + K + 1) - get(P, m, n, i - K, j + K + 1) - get(P, m, n, i + K + 1, j - K) + get(P, m, n, i - K, j - K);
            }
        }
        return ans;
    }
};

int main()
{
    Solution s;
    system("pause");
};