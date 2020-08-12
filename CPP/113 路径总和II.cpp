#include "include.hpp"
using namespace std;
/*
113. 路径总和 II
给定一个二叉树和一个目标和，找到所有从根节点到叶子节点路径总和等于给定目标和的路径。

说明: 叶子节点是指没有子节点的节点。

示例:
给定如下二叉树，以及目标和 sum = 22，

              5
             / \
            4   8
           /   / \
          11  13  4
         /  \    / \
        7    2  5   1
返回:

[
   [5,4,11,2],
   [5,8,4,5]
]
*/

/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode(int x) : val(x), left(NULL), right(NULL) {}
 * };
 */
class Solution {
    public:
    vector<vector<int>> res{};
    vector<vector<int>> pathSum(TreeNode* root, int sum) {
        pathSumPart(root,sum,vector<int>());
        return res;
    }

    void pathSumPart(TreeNode* root, int sum,vector<int>& p) {
        if(root == nullptr) return;
        p.push_back(root->val);
        if(root->left == nullptr && root->right== nullptr && sum-root->val == 0)
        {
            res.push_back(p);
        }
        pathSumPart(root->left,sum - root->val,p);
        pathSumPart(root->right,sum - root->val,p);
        p.pop_back();
    }
};

class Solution {
    public:
    vector<vector<int>> res{};
    vector<vector<int>> pathSum(TreeNode* root, int sum) {
        return  *pathSumPart(root,sum);
    }

    vector<vector<int>>* pathSumPart(TreeNode* root, int sum) {
        if(root == nullptr) return nullptr;
        if(root->left == nullptr && root->right== nullptr && sum-root->val == 0)
        {
            return new vector<vector<int>>{vector<int>{root->val}};
        }
        vector<vector<int>>* pl =  pathSumPart(root->left,sum - root->val);
        vector<vector<int>>* pr = pathSumPart(root->right,sum - root->val);
        vector<vector<int>>* rtn = new vector<vector<int>>();
        if(!pl)
        {
            for(auto x:*pl)
            {
                x.push_back(root->val);
                rtn->push_back(x);
            }
        }

        if(!pr)
        {
            for(auto x:*pr)
            {
                x.push_back(root->val);
                rtn->push_back(x);
            }
        }

        return rtn;
    }
};

int main()
{
    Solution s;
    system("pause");
};