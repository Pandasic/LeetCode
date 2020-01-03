"""
5296. 两棵二叉搜索树中的所有元素 显示英文描述 
用户通过次数91
用户尝试次数114
通过次数97
提交次数133
题目难度Medium
给你 root1 和 root2 这两棵二叉搜索树。

请你返回一个列表，其中包含 两棵树 中的所有整数并按 升序 排序。.

 

示例 1：

输入：root1 = [2,1,4], root2 = [1,0,3]
输出：[0,1,1,2,3,4]
示例 2：

输入：root1 = [0,-10,10], root2 = [5,1,7,0,2]
输出：[-10,0,0,1,2,5,7,10]
示例 3：

输入：root1 = [], root2 = [5,1,7,0,2]
输出：[0,1,2,5,7]
示例 4：

输入：root1 = [0,-10,10], root2 = []
输出：[-10,0,10]
示例 5：



输入：root1 = [1,null,8], root2 = [8,1]
输出：[1,1,8,8]
 

提示：

每棵树最多有 5000 个节点。
每个节点的值在 [-10^5, 10^5] 之间。

"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class BT():
    def __init__(self,node):
        self.root = node
        self.elements = []

    def LDR(self,node):
        if node == None:
            return
        self.LDR(node.left)
        self.elements += [node.val]
        self.LDR(node.right)
        return self.elements

class Solution:
    def getAllElements(self, root1: TreeNode, root2: TreeNode):
        eles = []
        bt1 = BT(root1)
        bt1.LDR(bt1.root)
        bt2 = BT(root2)
        bt2.LDR(bt2.root)
        eles = bt1.elements + bt2.elements
        eles.sort()
        return eles