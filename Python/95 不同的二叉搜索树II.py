"""
95. 不同的二叉搜索树 II
给定一个整数 n，生成所有由 1 ... n 为节点所组成的二叉搜索树。

示例:

输入: 3
输出:
[
  [1,null,3,2],
  [3,2,null,1],
  [3,1,null,null,2],
  [2,1,3],
  [1,null,2,null,3]
]
解释:
以上的输出对应以下 5 种不同结构的二叉搜索树：

   1         3     3      2      1
    \       /     /      / \      \
     3     2     1      1   3      2
    /     /       \                 \
   2     1         2                 3
通过次数25,353提交次数40,684
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

"""
class Solution:
    def __init__(self):
        self.res = []
        self.num = 0

    def generateTrees(self, n: int):
        self.num = n
        tree = [None,0]+[None for i in range(2**(n - 1) + 1)]
        self.generateTrees_part(tree,1,1)
        print(self.res)

    def generateTrees_part(self,tree,rootIndex,numCount):
        "
        #rootIndex :当前根节点
        #numCount  :当前已经填充的数字个树
        "
        if numCount == self.num:
            self.res.append(tree)
            return
        
        #仅填充左子树
        newTree = tree[:]
        newTree[rootIndex * 2] = newTree[rootIndex] - 1
        self.generateTrees_part(newTree, rootIndex * 2  - 1,numCount+1)
        #仅填充右子树
        newTree = tree[:]
        newTree[ rootIndex * 2 + 1 ] = newTree[rootIndex] + 1
        self.generateTrees_part(newTree,rootIndex * 2 + 1 ,numCount+1)
        #填充左右子树
        if numCount <= self.num - 2:
            newTree = tree[:]
            newTree[rootIndex * 2 + 1] = newTree[rootIndex] - 1
            newTree[rootIndex * 2  ] = newTree[rootIndex] + 1
            self.generateTrees_part(newTree,rootIndex * 2 + 1,numCount+2)
            self.generateTrees_part(newTree,rootIndex * 2  ,numCount+2)
"""

class Solution(object):
    def generateTrees(self, n):
        """
        :type n: int
        :rtype: List[TreeNode]
        """


"""
"""
"""
class Solution {
public:
    vector<TreeNode *> generateTrees(int n) {
        if (n) return generate(1, n);
        else return vector<TreeNode *>{};
    }
    
    vector<TreeNode *> generate(int left, int right) {
        vector<TreeNode *> ans;
        if (left > right) {
            ans.push_back(NULL);
            return ans;
        }
        for (int i = left; i <= right; i++) {
            vector<TreeNode *> left_nodes = generate(left, i - 1);
            vector<TreeNode *> right_nodes = generate(i + 1, right);
            for (TreeNode *left_node : left_nodes) {
                for (TreeNode *right_node : right_nodes) {
                    TreeNode *t = new TreeNode(i);
                    t->left = left_node;
                    t->right = right_node;
                    ans.push_back(t);
                }
            }
        }
        return ans;
    }
};
"""
s = Solution()
s.generateTrees(3)