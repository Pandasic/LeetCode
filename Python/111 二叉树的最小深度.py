"""
111. 二叉树的最小深度
给定一个二叉树，找出其最小深度。

最小深度是从根节点到最近叶子节点的最短路径上的节点数量。

说明: 叶子节点是指没有子节点的节点。

示例:

给定二叉树 [3,9,20,null,null,15,7],

    3
   / \
  9  20
    /  \
   15   7
返回它的最小深度  2.

通过次数64,380提交次数153,493
在真实的面试中遇到过这道题？
"""
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        res = []
        if not root:
            return 0
        def LDR (root,depth):
            if root == None:
                return
            if root.left is None and root.right is None:
                res.append(depth)
            else:
                LDR(root.left,depth + 1)
                LDR(root.right,depth + 1)
        
        LDR(root,0)
        return min(res) + 1