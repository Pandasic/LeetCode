#include "include.hpp"
using namespace std;
/*
199. 二叉树的右视图
给定一棵二叉树，想象自己站在它的右侧，按照从顶部到底部的顺序，返回从右侧所能看到的节点值。

示例:

输入: [1,2,3,null,5,null,4]
输出: [1, 3, 4]
解释:

   1            <---
 /   \
2     3         <---
 \     \
  5     4       <---
通过次数51,306提交次数80,387
在真实的面试中遇到过这道题？
*/
/*
深度优先
*/
class Solution {
public:
    vector<int> rightSideView(TreeNode* root) {
        vector<int> res;
        dfs(root,0,res);
        return res;
    }

    int dfs(TreeNode* root,int depth,vector<int>& res)
    {
        if(res.size()<depth + 1)
        {
            res.push_back(root->val);
        }
        dfs(root->right,depth+1,res);
        dfs(root->left,depth+1,res);
    }
};

/*广度优先*/
class Solution2{
public:
    vector<int> rightSideView(TreeNode* root) {
        vector<int> ans;
        if(!root)
            return ans;
        TreeNode* lastNode = root, *newLastNode = NULL;
        queue<TreeNode*> q;
        q.push(root);
        while(!q.empty()){
            TreeNode* curNode = q.front();
            q.pop();
            if(curNode->left){
                q.push(curNode->left);
                newLastNode = curNode->left;
            }
            if(curNode->right){
                q.push(curNode->right);
                newLastNode = curNode->right;
            }
            if(curNode == lastNode){
                ans.push_back(curNode->val);
                lastNode = newLastNode;
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