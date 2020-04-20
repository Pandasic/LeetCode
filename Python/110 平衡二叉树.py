"""
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

 

通过次数64,139提交次数125,623
"""
import tools
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class mySolution(object):
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        res = True
        def part(root: TreeNode,depth):
            if root == None:
                return depth
            lDepth = part(root.left,depth + 1)
            rDepth = part(root.right,depth + 1)
            if abs(lDepth - rDepth) > 1:
                res = False
            return max(lDepth,rDepth)

        part(root,0)
        return res

class Solution:
    # 自顶向下递归计算子树的高度
    def height(self, root: TreeNode) -> int:
        # 空树返回 -1
        if not root:
            return -1
        return 1 + max(self.height(root.left), self.height(root.right))
    
    def isBalanced(self, root: TreeNode) -> bool:
        # 空树也是平衡二叉树
        if not root:
            return True

        # 递归验证左子树高度和右子树高度之差的绝对值是否小于2
        # 同时左子树和右子树必须都为平衡二叉树
        return abs(self.height(root.left) - self.height(root.right)) < 2 \
            and self.isBalanced(root.left) \
            and self.isBalanced(root.right)

s = Solution()
print(
s.isBalanced(tools.stringToTreeNode(
    "[1,2,2,3,3,null,null,4,4]"))
)