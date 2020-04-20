"""
107. 二叉树的层次遍历 II
给定一个二叉树，返回其节点值自底向上的层次遍历。 （即按从叶子节点所在层到根节点所在的层，逐层从左向右遍历）

例如：
给定二叉树 [3,9,20,null,null,15,7],

    3
   / \
  9  20
    /  \
   15   7
返回其自底向上的层次遍历为：

[
  [15,7],
  [9,20],
  [3]
]
通过次数50,355提交次数77,793
"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def levelOrderBottom(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        res = {}

        def LDR (root,depth):
            if root == None:
                return
            if depth not in res.keys():
                res[depth] = [root.val]
            else:
                res[depth].append(root.val)
            LDR(root.left,depth + 1)
            LDR(root.right,depth + 1)
        
        LDR(root,0)
        res = res.values()
        res.reverse()
        return res