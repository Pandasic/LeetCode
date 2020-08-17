#include "include.hpp"
using namespace std;
/*
110. 平衡二叉树
给定一个二叉树，判断它是否是高度平衡的二叉树。

本题中，一棵高度平衡二叉树定义为：

一个二叉树每个节点 的左右两个子树的高度差的绝对值不超过1。

示例 1:

给定二叉树 [3,9,20,null,null,15,7]

    3
   / \
  9  20
    /  \
   15   7
返回 true 。

示例 2:

给定二叉树 [1,2,2,3,3,null,null,4,4]

       1
      / \
     2   2
    / \
   3   3
  / \
 4   4
返回 false 。

 

通过次数107,274提交次数200,394
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
    bool isBalanced(TreeNode* root) {
        return _isBalanced(root) != -1;
    }

    int _isBalanced(TreeNode* root) {
        if(root == NULL) return 0;

        int  left = _isBalanced(root->left);
        int right = _isBalanced(root->right);

        if(left == -1 || right == -1)
            return -1;
        
        if (abs(left - right) > 1)
            return -1;

        return max(left,right) + 1;

    }

};
int main()
{
    Solution s;
    system("pause");
};  