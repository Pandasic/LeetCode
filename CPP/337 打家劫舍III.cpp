#include "include.hpp"
using namespace std;
/*
337. 打家劫舍 III
在上次打劫完一条街道之后和一圈房屋后，小偷又发现了一个新的可行窃的地区。这个地区只有一个入口，我们称之为“根”。 除了“根”之外，每栋房子有且只有一个“父“房子与之相连。一番侦察之后，聪明的小偷意识到“这个地方的所有房屋的排列类似于一棵二叉树”。 如果两个直接相连的房子在同一天晚上被打劫，房屋将自动报警。

计算在不触动警报的情况下，小偷一晚能够盗取的最高金额。

示例 1:

输入: [3,2,3,null,3,null,1]

     3
    / \
   2   3
    \   \ 
     3   1

输出: 7 
解释: 小偷一晚能够盗取的最高金额 = 3 + 3 + 1 = 7.
示例 2:

输入: [3,4,5,1,3,null,1]

     3
    / \
   4   5
  / \   \ 
 1   3   1

输出: 9
解释: 小偷一晚能够盗取的最高金额 = 4 + 5 = 9.
通过次数55,540提交次数93,509
在真实的面试中遇到过这道题？
*/

/*递归 + 记录数组*/
class Solution {
public:
    unordered_map<TreeNode*,int> dp;
    int rob(TreeNode* root) {
        return _rob(root,false);
    }

    int _rob(TreeNode* root,bool isLastRobbed = false)
    {
        if(root == nullptr)
            return 0;
        int res = 0;
        if(isLastRobbed)
        {
            return _rob(root->left,false)+ _rob(root->right,false);
        }
        else
        {
            if(dp[root] != 0)
                return dp[root];
            int res = max(
                _rob(root->left,false) + _rob(root->right,false),
                _rob(root->left,true ) + _rob(root->right,true ) + root->val
            );
            dp[root] = res;
            return res;
        }
    }
};

/*官方DP f代表选择该节点 g 代表不选择*/
class Solution {
public:
    unordered_map <TreeNode*, int> f, g;

    void dfs(TreeNode* o) {
        if (!o) {
            return;
        }
        dfs(o->left);
        dfs(o->right);
        f[o] = o->val + g[o->left] + g[o->right];
        g[o] = max(f[o->left], g[o->left]) + max(f[o->right], g[o->right]);
    }

    int rob(TreeNode* o) {
        dfs(o);
        return max(f[o], g[o]);
    }
};

int main()
{
    Solution s;
    system("pause");
};