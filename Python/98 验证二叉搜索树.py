"""
98. 验证二叉搜索树
给定一个二叉树，判断其是否是一个有效的二叉搜索树。

假设一个二叉搜索树具有如下特征：

节点的左子树只包含小于当前节点的数。
节点的右子树只包含大于当前节点的数。
所有左子树和右子树自身必须也是二叉搜索树。
示例 1:

输入:
    2
   / \
  1   3
输出: true
示例 2:

输入:
    5
   / \
  1   4
     / \
    3   6
输出: false
解释: 输入为: [5,1,4,null,null,3,6]。
     根节点的值为 5 ，但是其右子节点值为 4 。
通过次数85,944提交次数290,380
在真实的面试中遇到过这道题？
"""
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


#框定范围 然后检测
class Solution(object):
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not root:
            return True
        def ser(rt,min,max):
            if (min!=None and rt.val<=min) or (max!=None and rt.val>=max):
                return False
            if rt.left:
                if rt.val<=rt.left.val or not ser(rt.left,min,rt.val):
                    return False
            if rt.right:
                if rt.val>=rt.right.val or not ser(rt.right,rt.val,max):
                    return False
            return True
        return ser(root,None,None)
        