#include "include.hpp"
using namespace std;
/*
437. 路径总和 III
给定一个二叉树，它的每个结点都存放着一个整数值。

找出路径和等于给定数值的路径总数。

路径不需要从根节点开始，也不需要在叶子节点结束，但是路径方向必须是向下的（只能从父节点到子节点）。

二叉树不超过1000个节点，且节点数值范围是 [-1000000,1000000] 的整数。

示例：

root = [10,5,-3,3,2,null,11,3,-2,null,1], sum = 8

      10
     /  \
    5   -3
   / \    \
  3   2   11
 / \   \
3  -2   1

返回 3。和等于 8 的路径有:

1.  5 -> 3
2.  5 -> 2 -> 1
3.  -3 -> 11
通过次数40,917提交次数73,891
*/
/*遍历+不定中鼎*/
/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode(int x) : val(x), left(NULL), right(NULL) {}
 * };
 */
/*双重递归*/
class Solution {
public:
    int orSum  = 0;
    int pathSum(TreeNode* root, int sum) {
        orSum = sum;
        if(!root) return 0;
        int res =0;
        res += pathSumPart(root,sum);
        res += pathSum(root->left,sum);
        res += pathSum(root->right,sum);
        return res;
    }

    int pathSumPart(TreeNode* root, int sum) {
        if(root == nullptr) return 0;
        sum -= root->val;
        int res = 0;
        if(sum == 0)
        {
            res += 1;
        }
        res += pathSumPart(root->left,sum);
        res += pathSumPart(root->right,sum);
        return res;
    };
};
int main()
{
    Solution s;
    system("pause");
};