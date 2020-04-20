"""
105. 从前序与中序遍历序列构造二叉树
根据一棵树的前序遍历与中序遍历构造二叉树。

注意:
你可以假设树中没有重复的元素。

例如，给出

前序遍历 preorder = [3,9,20,15,7]
中序遍历 inorder = [9,3,15,20,7]
返回如下的二叉树：

    3
   / \
  9  20
    /  \
   15   7
通过次数55,290提交次数85,448
在真实的面试中遇到过这道题？
"""
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """
        if not preorder: 
            return None
        
        x = preorder.pop(0)
        node = TreeNode(x)
        i = inorder.index(x)
        
        node.left = self.buildTree(preorder[:i], inorder[:i])
        node.right = self.buildTree(preorder[i:], inorder[i+1:])
        return node