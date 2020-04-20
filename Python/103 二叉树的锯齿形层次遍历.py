"""
103. 二叉树的锯齿形层次遍历
给定一个二叉树，返回其节点值的锯齿形层次遍历。（即先从左往右，再从右往左进行下一层遍历，以此类推，层与层之间交替进行）。

例如：
给定二叉树 [3,9,20,null,null,15,7],

    3
   / \
  9  20
    /  \
   15   7
返回锯齿形层次遍历如下：

[
  [3],
  [20,9],
  [15,7]
]
通过次数40,627提交次数75,208
在真实的面试中遇到过这道题？
"""
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def zigzagLevelOrder(self, root):
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
        for i in range(1,len(res),2):
            res[i].reverse()
        return res